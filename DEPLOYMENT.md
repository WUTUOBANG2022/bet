# 开发部署指南

## 本地开发环境

### 系统要求
- Python 3.8+
- Node.js 14+
- npm 6+

### 一键启动脚本

#### Windows (start.bat)
```batch
@echo off
cd backend
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python init_db.py
start http://localhost:8000/docs
python -m app.main

cd ..\frontend
call npm install
npm run dev
```

#### macOS/Linux (start.sh)
```bash
#!/bin/bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 init_db.py
open http://localhost:8000/docs
python3 -m app.main &

cd ../frontend
npm install
npm run dev
```

## 部署到生产环境

### Docker 部署

#### Dockerfile (后端)
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app ./app
COPY backend/init_db.py .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Dockerfile (前端)
```dockerfile
FROM node:18-alpine as build

WORKDIR /app

COPY frontend/package*.json ./
RUN npm ci

COPY frontend .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

#### docker-compose.yml
```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=sqlite:///./bet.db
      - SECRET_KEY=your-secret-key-here
    volumes:
      - ./backend:/app

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

  database:
    image: sqlite
    volumes:
      - db_data:/data

volumes:
  db_data:
```

### 使用Gunicorn和Nginx

#### 后端配置 (wsgi.py)
```python
from app.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

#### Nginx配置
```nginx
upstream backend {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name your-domain.com;

    location /api {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location / {
        root /var/www/betting-app/dist;
        try_files $uri $uri/ /index.html;
    }
}
```

## 环境配置

### .env 文件 (后端)
```
DEBUG=False
SECRET_KEY=your-super-secret-key-change-this-in-production
DATABASE_URL=sqlite:///./bet.db
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com
CORS_ORIGINS=https://your-domain.com
```

### .env 文件 (前端)
```
VITE_API_BASE_URL=https://api.your-domain.com
VITE_APP_NAME=BET系统
```

## 数据库迁移

### 使用Alembic (可选升级)

```python
# 安装Alembic
pip install alembic

# 初始化
alembic init migrations

# 创建迁移
alembic revision --autogenerate -m "Initial migration"

# 应用迁移
alembic upgrade head
```

## 监控和日志

### 日志配置
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### 性能监控
- 使用APM工具（如New Relic、DataDog）
- 监控API响应时间
- 监控数据库查询性能

## 备份和恢复

### SQLite备份
```bash
# 每日备份
0 2 * * * cp /app/bet.db /backups/bet_$(date +\%Y\%m\%d).db

# 定期清理旧备份
find /backups -name "bet_*.db" -mtime +30 -delete
```

## CI/CD 配置

### GitHub Actions 示例
```yaml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.11
    
    - name: Install dependencies
      run: |
        pip install -r backend/requirements.txt
    
    - name: Set up Node
      uses: actions/setup-node@v2
      with:
        node-version: 18
    
    - name: Build frontend
      run: |
        cd frontend
        npm install
        npm run build
    
    - name: Deploy
      run: |
        # 你的部署命令
```

## 故障排除

### 性能优化
1. 启用缓存（Redis）
2. 数据库索引优化
3. 前端资源压缩
4. 使用CDN

### 常见问题
- CORS错误：检查后端CORS配置
- 认证失败：检查JWT密钥
- 数据库锁定：检查并发问题

## 安全检查清单

- [ ] 修改默认密钥和密码
- [ ] 启用HTTPS
- [ ] 配置防火墙规则
- [ ] 启用数据库加密
- [ ] 定期安全更新
- [ ] 实施日志监控
- [ ] 备份关键数据
- [ ] 配置速率限制
