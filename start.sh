#!/bin/bash
set -e

# Railway 生产环境启动脚本
cd backend

# 初始化数据库
python3 init_db.py

# 启动 FastAPI 后端
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT
