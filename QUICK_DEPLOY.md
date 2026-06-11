# 🚀 5分钟快速部署卡

## 第1步：GitHub上传（2分钟）

```bash
# Windows PowerShell
cd c:\Users\21106\Desktop\bet

# 初始化Git
git init
git add .
git commit -m "Initial commit"

# 添加GitHub仓库（替换USERNAME/REPO）
git remote add origin https://github.com/USERNAME/REPO.git
git branch -M main
git push -u origin main
```

**需要创建GitHub账户？** → https://github.com/signup

---

## 第2步：Railway后端（1分钟）

1. 访问 → https://railway.app
2. 点击「Start Project」→ 用GitHub登录
3. 选择你的项目仓库
4. 配置：
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt && python init_db.py`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. 点击「Deploy」
6. 添加环境变量：
   ```
   SECRET_KEY = your-secret-key
   DATABASE_URL = sqlite:///./bet.db
   ```
7. 等待绿色✓ → 复制URL备用

---

## 第3步：Railway前端（1分钟）

1. 点击「+ New」→ GitHub Repo
2. 配置：
   - Root Directory: `frontend`
   - Build Command: `npm install && npm run build`
   - Start Command: `npm run preview`
3. 点击「Deploy」
4. 添加环境变量：
   ```
   VITE_API_BASE_URL = https://你的后端URL.railway.app
   ```
5. 等待绿色✓ → 复制URL

---

## 第4步：测试验证（1分钟）

```
1. 打开前端URL
2. 注册账户 (用户名: testuser / 密码: test123)
3. 登录
4. 查看比赛列表
5. 尝试下注
6. 检查钱包
```

---

## ✅ 部署完成！

| 内容 | URL |
|------|-----|
| 🎲 前端应用 | `https://your-frontend.railway.app` |
| 📡 后端API | `https://your-backend.railway.app` |
| 📚 API文档 | `https://your-backend.railway.app/docs` |

---

## 🎉 分享给朋友

```
嘿，我做了个下注应用！
快来试试：https://your-frontend.railway.app
每人初始¥1000，看谁能赚最多！🎲
```

---

## 🔑 关键密钥生成

```bash
# 生成安全的SECRET_KEY
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## ❌ 常见错误快速修复

| 错误 | 解决方案 |
|------|--------|
| 前端无法连接后端 | 检查VITE_API_BASE_URL环境变量 |
| 前端打不开 | 检查build日志，重新部署 |
| 后端无法启动 | 检查SECRET_KEY是否设置 |
| 数据库错误 | 确保DATABASE_URL正确 |

---

## 📞 需要帮助？

1. 查看完整文档：`DEPLOY_RAILWAY.md`
2. 查看API文档：`API.md`
3. 用户指南：`USER_GUIDE.md`

**祝部署顺利！** 🚀

