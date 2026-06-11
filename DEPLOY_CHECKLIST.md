# ✅ 部署前检查清单

在上线前，请按照以下清单检查项目：

## 代码准备

- [ ] 所有代码已提交到Git
- [ ] 没有敏感信息（密钥、密码）在代码中
- [ ] `.env` 文件已添加到 `.gitignore`
- [ ] 所有依赖都在 `requirements.txt` 和 `package.json` 中

## 后端检查

- [ ] ✅ `backend/requirements.txt` 包含所有依赖
- [ ] ✅ `backend/Procfile` 已配置
- [ ] ✅ `backend/runtime.txt` 已配置
- [ ] 数据库初始化脚本 (`init_db.py`) 可正常运行
- [ ] 环境变量已准备：
  - [ ] `SECRET_KEY`（生产环境密钥）
  - [ ] `DATABASE_URL`（默认：sqlite:///./bet.db）

## 前端检查

- [ ] ✅ `frontend/package.json` 包含所有依赖
- [ ] ✅ `frontend/Procfile` 已配置
- [ ] ✅ `frontend/vite.config.js` 已配置环境变量支持
- [ ] 环境变量已准备：
  - [ ] `VITE_API_BASE_URL`（后端URL）

## 部署步骤

### 步骤1：GitHub准备
- [ ] 创建GitHub账户（如未有）
- [ ] 创建新的Repository
- [ ] 将项目代码上传到GitHub

### 步骤2：Railway后端部署
- [ ] 注册Railway账户（railway.app）
- [ ] 连接GitHub授权
- [ ] 创建后端项目
  - [ ] Root Directory: `backend`
  - [ ] Build Command: 已配置
  - [ ] Start Command: 已配置
- [ ] 设置环境变量（SECRET_KEY, DATABASE_URL）
- [ ] 等待部署成功
- [ ] 复制后端URL：`https://_____.railway.app`

### 步骤3：Railway前端部署
- [ ] 创建前端项目
  - [ ] Root Directory: `frontend`
  - [ ] Build Command: 已配置
  - [ ] Start Command: 已配置
- [ ] 设置环境变量
  - [ ] `VITE_API_BASE_URL=https://_____.railway.app`
- [ ] 等待部署成功
- [ ] 复制前端URL：`https://_____.railway.app`

## 测试验证

- [ ] 打开前端URL能正常加载
- [ ] 能够注册新账户
- [ ] 能够登录
- [ ] 能够查看比赛列表
- [ ] 能够进行下注
- [ ] 能够查看钱包余额
- [ ] 能够查看交易记录

## 上线准备

- [ ] 生成强密钥用于SECRET_KEY
  ```bash
  python -c "import secrets; print(secrets.token_hex(32))"
  ```
- [ ] 检查CORS配置是否正确
- [ ] 检查错误日志是否正常
- [ ] 准备分享链接给朋友
- [ ] 准备使用指南文档

## 分享给朋友

- [ ] 复制前端URL
- [ ] 准备简短的介绍
- [ ] 分享USER_GUIDE.md给新用户
- [ ] 收集反馈信息

## 上线后维护

- [ ] 定期检查Railway Dashboard
- [ ] 监控错误日志
- [ ] 收集用户反馈
- [ ] 定期备份数据库
- [ ] 处理问题和Bug修复

---

**所有项都打勾后，就可以上线了！** 🚀
