from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.models import User, Match, Bet, Transaction
from app.routes import auth_router, matches_router, bets_router, users_router

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(title="赌博比赛下注系统")

# CORS中间件配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(auth_router)
app.include_router(matches_router)
app.include_router(bets_router)
app.include_router(users_router)

@app.get("/")
def read_root():
    return {"message": "欢迎使用赌博比赛下注系统"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
