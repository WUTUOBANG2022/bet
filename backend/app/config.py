from pydantic_settings import BaseSettings
from datetime import timedelta

class Settings(BaseSettings):
    # JWT设置
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # 数据库
    DATABASE_URL: str = "sqlite:///./bet.db"
    
    class Config:
        env_file = ".env"

settings = Settings()
