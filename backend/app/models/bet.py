from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Bet(Base):
    __tablename__ = "bets"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    match_id = Column(Integer, ForeignKey("matches.id"))
    choice = Column(String)  # A, B, 或 draw
    amount = Column(Float)  # 下注金额
    odds = Column(Float)  # 下注时的赔率
    potential_payout = Column(Float)  # 潜在收益
    result = Column(String, nullable=True)  # pending, won, lost
    winnings = Column(Float, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    settled_at = Column(DateTime, nullable=True)
    
    # 关系
    user = relationship("User", back_populates="bets")
    match = relationship("Match", back_populates="bets")
