from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 用户相关
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    balance: float
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

# 比赛相关
class MatchCreate(BaseModel):
    title: str
    team_a: str
    team_b: str
    odds_a: float
    odds_b: float
    odds_draw: float
    start_time: datetime

class MatchUpdate(BaseModel):
    score_a: int
    score_b: int
    winner: Optional[str] = None
    status: str

class MatchResponse(BaseModel):
    id: int
    title: str
    team_a: str
    team_b: str
    odds_a: float
    odds_b: float
    odds_draw: float
    status: str
    start_time: datetime
    end_time: Optional[datetime]
    score_a: int
    score_b: int
    winner: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

# 下注相关
class BetCreate(BaseModel):
    match_id: int
    choice: str  # A, B, draw
    amount: float

class BetResponse(BaseModel):
    id: int
    user_id: int
    match_id: int
    choice: str
    amount: float
    odds: float
    potential_payout: float
    result: Optional[str]
    winnings: float
    created_at: datetime
    settled_at: Optional[datetime]
    
    class Config:
        from_attributes = True

# 交易相关
class TransactionResponse(BaseModel):
    id: int
    user_id: int
    type: str
    amount: float
    description: Optional[str]
    balance_after: float
    created_at: datetime
    
    class Config:
        from_attributes = True
