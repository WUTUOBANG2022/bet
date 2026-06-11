#!/usr/bin/env python3
"""
初始化脚本：创建测试数据
"""
from app.database import SessionLocal
from app.models import User, Match
from app.auth import get_password_hash
from datetime import datetime, timedelta

def init_db():
    db = SessionLocal()
    
    # 创建测试用户
    user1 = User(
        username="testuser1",
        email="test1@example.com",
        hashed_password=get_password_hash("password123"),
        balance=5000.0
    )
    user2 = User(
        username="testuser2",
        email="test2@example.com",
        hashed_password=get_password_hash("password123"),
        balance=3000.0
    )
    
    # 创建测试比赛
    match1 = Match(
        title="英超：曼联 vs 曼城",
        team_a="曼联",
        team_b="曼城",
        odds_a=2.5,
        odds_b=1.8,
        odds_draw=3.0,
        start_time=datetime.utcnow() + timedelta(hours=2),
        status="pending"
    )
    
    match2 = Match(
        title="欧冠：利物浦 vs 皇马",
        team_a="利物浦",
        team_b="皇马",
        odds_a=2.0,
        odds_b=2.2,
        odds_draw=3.2,
        start_time=datetime.utcnow() + timedelta(hours=4),
        status="pending"
    )
    
    db.add_all([user1, user2, match1, match2])
    db.commit()
    print("数据库已初始化！")

if __name__ == "__main__":
    init_db()
