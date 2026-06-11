@echo off
echo 启动赌博比赛下注系统...
echo.

REM 启动后端
cd backend
echo 正在启动后端服务器...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python init_db.py
start http://localhost:8000/docs
python -m app.main &
cd ..

REM 启动前端
cd frontend
echo 正在启动前端服务器...
call npm install
call npm run dev
cd ..

echo.
echo 系统已启动！
echo 后端: http://localhost:8000
echo 前端: http://localhost:5173
echo API文档: http://localhost:8000/docs
pause
