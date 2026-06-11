# 🚀 为WUTUOBANG2022生成的一键部署配置

## 你的部署信息

```
GitHub用户名: WUTUOBANG2022
仓库名称: bet
应用名称: 赌博下注系统
```

---

## 📋 一键部署步骤

### 第1步：初始化Git并推送到GitHub

在PowerShell中运行以下命令：

```powershell
# 进入项目目录
cd c:\Users\21106\Desktop\bet

# 初始化Git
git init
git add .
git commit -m "Initial commit: Betting app"

# 添加远程仓库
git remote add origin https://github.com/WUTUOBANG2022/bet.git

# 推送代码
git branch -M main
git push -u origin main
```

**注意：** 首次push时会弹出GitHub认证窗口，用浏览器登录即可。

---

### 第2步：在Railway中部署后端

1. **访问 https://railway.app**

2. **点击 「Start Project」** → 用GitHub登录

3. **选择仓库**
   - 选择 `WUTUOBANG2022/bet`

4. **配置后端服务**
   ```
   Name: betting-backend
   Root Directory: backend
   ```

5. **设置Build和Start命令**（应该自动检测，确认如下）
   ```
   Build: pip install -r requirements.txt && python init_db.py
   Start: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

6. **添加环境变量**
   ```
   SECRET_KEY = sk_live_$(date +%s)_$(openssl rand -hex 32)
   DATABASE_URL = sqlite:///./bet.db
   CORS_ORIGINS = *
   ```

7. **点击「Deploy」** 等待✓

8. **复制后端URL**
   ```
   格式: https://xxx-xxx-xxx.railway.app
   ```

---

### 第3步：在Railway中部署前端

1. **在同一个项目中点击「+ New」**

2. **选择「GitHub Repo」** → 选择 `WUTUOBANG2022/bet`

3. **配置前端服务**
   ```
   Name: betting-frontend
   Root Directory: frontend
   ```

4. **设置Build和Start命令**
   ```
   Build: npm install && npm run build
   Start: npm run preview
   ```

5. **添加环境变量**
   ```
   VITE_API_BASE_URL = https://[你的后端URL].railway.app
   PORT = 3000
   ```

6. **点击「Deploy」** 等待✓

7. **复制前端URL** 
   ```
   格式: https://yyy-yyy-yyy.railway.app
   ```

---

## ✅ 验证部署成功

打开前端URL，测试：
- [ ] 能正常加载页面
- [ ] 能注册账户
- [ ] 能登录
- [ ] 能查看比赛列表
- [ ] 能进行下注
- [ ] 能查看钱包

---

## 🎉 分享给朋友

```
🎲 新应用上线啦！

我做了个赌博比赛下注模拟系统！
每人初始¥1000，看谁能赚最多！

👉 打开这个链接立即体验：
https://[你的前端URL].railway.app

还不赶快来试试？ 🚀
```

---

## 🔧 部署后的管理

### 查看后端API文档
```
https://[你的后端URL].railway.app/docs
```

### 查看Railway Dashboard
```
https://railway.app/dashboard
```

### GitHub仓库
```
https://github.com/WUTUOBANG2022/bet
```

---

## 📱 常见问题速解

| 问题 | 解决方案 |
|------|--------|
| 前端无法连接后端 | 检查`VITE_API_BASE_URL`是否正确 |
| 部署超时 | 等待5-10分钟，免费版本较慢 |
| 数据库错误 | 检查`DATABASE_URL`是否为`sqlite:///./bet.db` |
| 无法登录 | 清除浏览器缓存，刷新重试 |

---

## 需要帮助？

1. **部署卡住？** → 查看Railway Dashboard的日志
2. **API错误？** → 访问`https://[后端URL]/docs`测试端点
3. **功能问题？** → 查看`USER_GUIDE.md`

---

**祝部署顺利！** 🚀✨

