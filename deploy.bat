@echo off
REM 🚀 一键部署脚本（Windows）

echo.
echo ╔════════════════════════════════════════════════╗
echo ║   🚀 赌博下注应用一键部署                     ║
echo ║   Betting App Auto Deploy                      ║
echo ╚════════════════════════════════════════════════╝
echo.

REM 检查Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 未找到Python，请先安装Python
    echo 下载地址：https://www.python.org/downloads/
    pause
    exit /b 1
)

REM 检查Git
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 未找到Git，请先安装Git
    echo 下载地址：https://git-scm.com/
    pause
    exit /b 1
)

REM 运行部署脚本
python deploy.py
pause
