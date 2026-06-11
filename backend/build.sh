#!/bin/bash
set -e

# 安装Python依赖
cd backend
pip install -r requirements.txt
python init_db.py
cd ..

echo "后端准备完成"
