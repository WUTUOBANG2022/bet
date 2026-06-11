from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum

class MatchStatus(str, enum.Enum):
    PENDING = "pending"
    LIVE = "live"
    FINISHED = "finished"
    CANCELLED = "cancelled"

class Match(Base):
    __tablename__ = "matches"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)  # 比赛标题
    team_a = Column(String)  # A队
    team_b = Column(String)  # B队
    odds_a = Column(Float, default=1.5)  # A队赔率
    odds_b = Column(Float, default=1.5)  # B队赔率
    odds_draw = Column(Float, default=3.0)  # 平局赔率
    status = Column(String, default=MatchStatus.PENDING)  # pending, live, finished, cancelled
    start_time = Column(DateTime)
    end_time = Column(DateTime, nullable=True)
    score_a = Column(Integer, default=0)
    score_b = Column(Integer, default=0)
    winner = Column(String, nullable=True)  # A, B, 或 draw
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # 关系
    bets = relationship("Bet", back_populates="match")
