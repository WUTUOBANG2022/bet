# 🚀 快速上线指南（Railway.app）

**预计时间：5-10分钟**  
**成本：完全免费**  
**用户数：最多支持小型项目**

## 方案对比

| 方案 | 成本 | 难度 | 速度 | 推荐指数 |
|-----|------|------|------|--------|
| **Railway** | 免费 | ⭐ | 5分钟 | ⭐⭐⭐⭐⭐ |
| Render | 免费 | ⭐⭐ | 10分钟 | ⭐⭐⭐⭐ |
| Heroku | 付费 | ⭐ | 5分钟 | ⭐⭐⭐ |
| 自建VPS | $5/月 | ⭐⭐⭐ | 30分钟 | ⭐⭐⭐ |

## 完整部署步骤

### 第一步：准备GitHub账户

1. 访问 https://github.com/signup
2. 注册GitHub账户（如已有跳过）
3. 创建新的Repository

### 第二步：上传项目到GitHub

```bash
# 1. 进入项目目录
cd c:\Users\21106\Desktop\bet

# 2. 初始化Git
git init

# 3. 添加所有文件
git add .

# 4. 提交
git commit -m "Initial commit: Betting app"

# 5. 添加远程仓库（替换USERNAME和REPO）
git remote add origin https://github.com/USERNAME/REPO.git

# 6. 推送到GitHub
git branch -M main
git push -u origin main
```

### 第三步：在Railway上部署后端

1. **访问 https://railway.app**
   - 点击「Start Project」
   - 用GitHub账户登录

2. **创建后端服务**
   - 选择「Deploy from GitHub repo」
   - 选择你的项目仓库
   - 配置如下：

   ```
   Root Directory: backend
   Build Command: pip install -r requirements.txt && python init_db.py
   Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

3. **设置环境变量**
   - 点击「Variables」标签
   - 添加：
   ```
   SECRET_KEY=your-super-secret-key-123456789
   DATABASE_URL=sqlite:///./bet.db
   ```

4. **等待部署完成**
   - 看到绿色✓就表示成功
   - 复制生成的后端URL（如：https://xxx.railway.app）

### 第四步：在Railway上部署前端

1. **创建新服务**
   - 点击「+ New」
   - 选择「GitHub Repo」
   - 配置如下：

   ```
   Root Directory: frontend
   Build Command: npm install && npm run build
   Start Command: npm run preview
   ```

2. **设置环境变量**
   - 添加：
   ```
   VITE_API_BASE_URL=https://your-backend-url.railway.app
   ```
   （用第三步得到的后端URL替换）

3. **等待部署完成**
   - 复制生成的前端URL（如：https://yyy.railway.app）

### 第五步：验证部署

1. **打开前端**：https://yyy.railway.app
2. **测试登录**：
   - 用户名：testuser1
   - 密码：password123
3. **测试下注功能**

## 分享给朋友

部署完成后，只需给朋友们分享：
```
🎲 赌博比赛下注系统上线啦！
访问链接：https://yyy.railway.app
```

## 常见问题

### Q: 前端打不开？
```
1. 检查VITE_API_BASE_URL环境变量是否正确
2. 在浏览器F12查看Console是否有错误
3. 重新部署前端
```

### Q: 后端出错？
```
1. 在Railway查看Logs
2. 检查SECRET_KEY是否设置
3. 检查环境变量是否正确
```

### Q: 数据库问题？
```
1. Railway会自动持久化SQLite数据库
2. 数据不会丢失
```

### Q: 访问速度慢？
```
1. 免费版本会有冷启动延迟
2. 访问后会变快
```

## 升级为付费（可选）

如果朋友们太多，可以升级Railway账户：
- Railway提供免费额度
- 超过后按实际使用付费（通常$5/月起）

## 其他免费选项

### 方案B：Render.com
```
1. https://render.com 注册
2. 创建后端服务（Railway同样步骤）
3. 创建前端服务（Railway同样步骤）
4. 特点：同样免费，稳定性略好
```

### 方案C：Replit.com
```
1. https://replit.com 注册
2. Fork这个项目
3. 点击Run自动启动
4. 特点：最简单但性能一般
```

## 监控和维护

### 查看日志
- 在Railway Dashboard查看实时日志
- 监控错误和性能

### 定期备份
- Railway会自动备份
- 也可以定期下载数据库文件

### 更新应用
```bash
# 本地修改代码后
git add .
git commit -m "Update features"
git push origin main

# Railway会自动重新部署
```

## 安全建议

⚠️ **生产环境安全：**

1. **修改SECRET_KEY**
   ```
   生成新的密钥：
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

2. **配置CORS**
   ```
   在app/main.py中修改allow_origins
   只允许你的前端URL
   ```

3. **启用HTTPS**
   ```
   Railway自动为所有应用启用HTTPS
   ```

4. **定期检查日志**
   ```
   查找异常登录或请求
   ```

5. **备份重要数据**
   ```
   定期导出比赛和交易记录
   ```

## 成本总结

| 项目 | 成本 |
|-----|------|
| 域名 | $0（使用railway.app域名） |
| 服务器 | $0（免费额度） |
| 数据库 | $0（SQLite） |
| 总计 | **$0** |

---

**现在就开始吧！** 5分钟后你的朋友们就能使用了！🚀
