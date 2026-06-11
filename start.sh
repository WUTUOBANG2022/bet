#!/bin/bash

echo "启动赌博比赛下注系统..."
echo ""

# 启动后端
cd backend
echo "正在启动后端服务器..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 init_db.py
python3 -m app.main &
BACKEND_PID=$!
sleep 2
echo "后端服务器已启动 (PID: $BACKEND_PID)"
open http://localhost:8000/docs

cd ../frontend
echo "正在启动前端服务器..."
npm install
npm run dev

# 清理
kill $BACKEND_PID

echo ""
echo "系统已启动！"
echo "后端: http://localhost:8000"
echo "前端: http://localhost:5173"
echo "API文档: http://localhost:8000/docs"
