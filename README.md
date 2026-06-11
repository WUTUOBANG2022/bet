# 🎲 赌博比赛下注系统

完整的Web应用，支持创建比赛、下注、查看赔率、结果结算等功能。

## 功能特性

✅ **用户管理**
- 用户注册和登录（JWT认证）
- 用户余额和钱包管理
- 交易历史记录

✅ **比赛管理**
- 创建和管理比赛
- 设置赔率
- 更新比赛状态和结果

✅ **下注系统**
- 支持多种下注选择（A队、B队、平局）
- 实时赔率显示
- 下注金额验证

✅ **结算系统**
- 自动计算赢利
- 更新用户余额
- 记录交易历史

✅ **用户界面**
- 现代化的Vue.js前端
- 响应式设计
- 实时数据更新

## 技术栈

### 后端
- **Framework**: FastAPI
- **Database**: SQLite
- **Authentication**: JWT (python-jose)
- **ORM**: SQLAlchemy

### 前端
- **Framework**: Vue 3
- **Build Tool**: Vite
- **HTTP Client**: Axios
- **Routing**: Vue Router

## 项目结构

```
bet/
├── backend/
│   ├── app/
│   │   ├── models/           # 数据库模型
│   │   ├── routes/           # API路由
│   │   ├── auth.py           # 认证模块
│   │   ├── config.py         # 配置
│   │   ├── database.py       # 数据库连接
│   │   ├── schemas.py        # 数据验证模式
│   │   └── main.py           # FastAPI应用主文件
│   ├── requirements.txt      # Python依赖
│   └── init_db.py           # 数据库初始化
└── frontend/
    ├── src/
    │   ├── pages/            # 页面组件
    │   ├── components/       # 可复用组件
    │   ├── router.js         # 路由配置
    │   ├── App.vue           # 根组件
    │   └── main.js           # 入口文件
    ├── package.json          # NPM依赖
    └── vite.config.js        # Vite配置
```

## 快速开始

### 1. 后端设置

```bash
# 进入后端目录
cd backend

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 初始化数据库
python init_db.py

# 启动服务器
python -m app.main

# 或使用uvicorn
uvicorn app.main:app --reload
```

服务器将运行在 http://localhost:8000

### 2. 前端设置

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

应用将运行在 http://localhost:5173

## API 端点

### 认证
- `POST /auth/register` - 用户注册
- `POST /auth/login` - 用户登录

### 比赛
- `GET /matches` - 获取所有比赛
- `GET /matches/{match_id}` - 获取特定比赛
- `POST /matches/` - 创建比赛
- `PUT /matches/{match_id}` - 更新比赛

### 下注
- `POST /bets/` - 创建下注
- `GET /bets/user/{user_id}` - 获取用户下注
- `GET /bets/{bet_id}` - 获取特定下注

### 用户/钱包
- `GET /users/{user_id}` - 获取用户信息
- `GET /users/{user_id}/wallet` - 获取钱包余额
- `GET /users/{user_id}/transactions` - 获取交易记录
- `POST /users/{user_id}/deposit` - 存款
- `POST /users/{user_id}/withdraw` - 提现

## 测试账户

初始化数据库后，可使用以下测试账户：

| 用户名 | 密码 | 余额 |
|--------|------|------|
| testuser1 | password123 | 5000 |
| testuser2 | password123 | 3000 |

## 工作流程

1. **用户注册/登录** - 创建账户或登录
2. **浏览比赛** - 查看可用的比赛和赔率
3. **下注** - 选择下注选项和金额
4. **等待结果** - 比赛进行中
5. **结算** - 比赛结束，系统自动计算赢利
6. **查看交易** - 在钱包查看所有交易记录

## 数据模型

### User（用户）
- id, username, email, hashed_password, balance, is_active, created_at

### Match（比赛）
- id, title, team_a, team_b, odds_a, odds_b, odds_draw, status, start_time, end_time, score_a, score_b, winner

### Bet（下注）
- id, user_id, match_id, choice, amount, odds, potential_payout, result, winnings, created_at, settled_at

### Transaction（交易）
- id, user_id, type (deposit/withdrawal/bet/payout), amount, description, balance_after, created_at

## 安全性考虑

⚠️ **生产环境注意事项：**

1. 修改 `app/config.py` 中的 `SECRET_KEY`
2. 启用HTTPS
3. 配置适当的CORS政策
4. 添加速率限制
5. 实现完整的错误处理
6. 添加输入验证和清理
7. 使用环境变量管理敏感配置
8. 定期备份数据库

## 未来改进

- [ ] WebSocket实时比分更新
- [ ] 用户认证Token刷新机制
- [ ] 高级统计和分析
- [ ] 用户权限管理
- [ ] 数据分页和过滤
- [ ] 邮件通知系统
- [ ] 支付网关集成
- [ ] Docker部署配置

## 故障排除

### 后端无法启动
```bash
# 检查Python版本（需要3.8+）
python --version

# 重新安装依赖
pip install --upgrade -r requirements.txt
```

### 前端连接不到后端
- 检查后端服务是否运行在 http://localhost:8000
- 检查CORS配置

### 数据库错误
```bash
# 删除旧数据库
rm bet.db

# 重新初始化
python init_db.py
```

## 许可证

MIT License

## 支持

如有问题或建议，请提交Issue。
