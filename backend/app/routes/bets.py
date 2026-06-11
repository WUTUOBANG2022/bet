from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Bet, User, Match, Transaction
from app.schemas import BetCreate, BetResponse
from datetime import datetime

router = APIRouter(prefix="/bets", tags=["bets"])

@router.post("/", response_model=BetResponse)
def place_bet(bet: BetCreate, user_id: int, db: Session = Depends(get_db)):
    # 获取用户
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    
    # 检查余额
    if user.balance < bet.amount:
        raise HTTPException(status_code=400, detail="余额不足")
    
    # 获取比赛
    match = db.query(Match).filter(Match.id == bet.match_id).first()
    if not match:
        raise HTTPException(status_code=404, detail="比赛不存在")
    
    # 检查比赛状态
    if match.status != "pending" and match.status != "live":
        raise HTTPException(status_code=400, detail="比赛已结束或已取消")
    
    # 获取赔率
    if bet.choice == "A":
        odds = match.odds_a
    elif bet.choice == "B":
        odds = match.odds_b
    elif bet.choice == "draw":
        odds = match.odds_draw
    else:
        raise HTTPException(status_code=400, detail="无效的选择")
    
    # 创建下注
    db_bet = Bet(
        user_id=user_id,
        match_id=bet.match_id,
        choice=bet.choice,
        amount=bet.amount,
        odds=odds,
        potential_payout=bet.amount * odds,
        result="pending"
    )
    
    # 扣除用户余额
    user.balance -= bet.amount
    
    # 记录交易
    transaction = Transaction(
        user_id=user_id,
        type="bet",
        amount=bet.amount,
        description=f"在比赛 {match.title} 中下注 {bet.choice}",
        balance_after=user.balance
    )
    
    db.add(db_bet)
    db.add(transaction)
    db.commit()
    db.refresh(db_bet)
    return db_bet

@router.get("/user/{user_id}", response_model=list[BetResponse])
def get_user_bets(user_id: int, db: Session = Depends(get_db)):
    bets = db.query(Bet).filter(Bet.user_id == user_id).all()
    return bets

@router.get("/{bet_id}", response_model=BetResponse)
def get_bet(bet_id: int, db: Session = Depends(get_db)):
    bet = db.query(Bet).filter(Bet.id == bet_id).first()
    if not bet:
        raise HTTPException(status_code=404, detail="下注不存在")
    return bet
