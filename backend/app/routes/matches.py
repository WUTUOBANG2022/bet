from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Match, Bet, User, Transaction
from app.schemas import MatchCreate, MatchUpdate, MatchResponse
from datetime import datetime

router = APIRouter(prefix="/matches", tags=["matches"])

@router.post("/", response_model=MatchResponse)
def create_match(match: MatchCreate, db: Session = Depends(get_db)):
    db_match = Match(
        title=match.title,
        team_a=match.team_a,
        team_b=match.team_b,
        odds_a=match.odds_a,
        odds_b=match.odds_b,
        odds_draw=match.odds_draw,
        start_time=match.start_time,
        status="pending"
    )
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match

@router.get("/", response_model=list[MatchResponse])
def get_matches(status: str = None, db: Session = Depends(get_db)):
    query = db.query(Match)
    if status:
        query = query.filter(Match.status == status)
    return query.all()

@router.get("/{match_id}", response_model=MatchResponse)
def get_match(match_id: int, db: Session = Depends(get_db)):
    match = db.query(Match).filter(Match.id == match_id).first()
    if not match:
        raise HTTPException(status_code=404, detail="比赛不存在")
    return match

@router.put("/{match_id}", response_model=MatchResponse)
def update_match(match_id: int, match_update: MatchUpdate, db: Session = Depends(get_db)):
    db_match = db.query(Match).filter(Match.id == match_id).first()
    if not db_match:
        raise HTTPException(status_code=404, detail="比赛不存在")
    
    db_match.score_a = match_update.score_a
    db_match.score_b = match_update.score_b
    db_match.winner = match_update.winner
    db_match.status = match_update.status
    
    if match_update.status == "finished":
        db_match.end_time = datetime.utcnow()
        # 结算所有下注
        settle_bets(db_match.id, db)
    
    db.commit()
    db.refresh(db_match)
    return db_match

def settle_bets(match_id: int, db: Session):
    """结算该比赛的所有下注"""
    match = db.query(Match).filter(Match.id == match_id).first()
    if not match or not match.winner:
        return
    
    bets = db.query(Bet).filter(Bet.match_id == match_id, Bet.result == "pending").all()
    
    for bet in bets:
        if bet.choice == match.winner:
            # 赢了
            bet.result = "won"
            bet.winnings = bet.amount * bet.odds
            # 更新用户余额
            user = db.query(User).filter(User.id == bet.user_id).first()
            user.balance += bet.winnings
            # 记录交易
            transaction = Transaction(
                user_id=bet.user_id,
                type="payout",
                amount=bet.winnings,
                description=f"比赛 {match.title} 下注赢利",
                balance_after=user.balance
            )
            db.add(transaction)
        else:
            # 输了
            bet.result = "lost"
            bet.winnings = 0
        
        bet.settled_at = datetime.utcnow()
        db.add(bet)
    
    db.commit()
