from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Transaction
from app.schemas import UserResponse, TransactionResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user

@router.get("/{user_id}/wallet")
def get_wallet(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return {"balance": user.balance}

@router.get("/{user_id}/transactions", response_model=list[TransactionResponse])
def get_transactions(user_id: int, db: Session = Depends(get_db)):
    transactions = db.query(Transaction).filter(
        Transaction.user_id == user_id
    ).order_by(Transaction.created_at.desc()).all()
    return transactions

@router.post("/{user_id}/deposit")
def deposit(user_id: int, amount: float, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    
    if amount <= 0:
        raise HTTPException(status_code=400, detail="金额必须大于0")
    
    user.balance += amount
    
    transaction = Transaction(
        user_id=user_id,
        type="deposit",
        amount=amount,
        description="存款",
        balance_after=user.balance
    )
    
    db.add(transaction)
    db.commit()
    
    return {"balance": user.balance, "amount": amount}

@router.post("/{user_id}/withdraw")
def withdraw(user_id: int, amount: float, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    
    if amount <= 0:
        raise HTTPException(status_code=400, detail="金额必须大于0")
    
    if user.balance < amount:
        raise HTTPException(status_code=400, detail="余额不足")
    
    user.balance -= amount
    
    transaction = Transaction(
        user_id=user_id,
        type="withdrawal",
        amount=amount,
        description="提现",
        balance_after=user.balance
    )
    
    db.add(transaction)
    db.commit()
    
    return {"balance": user.balance, "amount": amount}
