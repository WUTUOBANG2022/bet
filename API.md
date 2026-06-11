# 赌博比赛下注系统 - API文档

所有API端点都需要进行相应的认证和数据验证。

## 基础信息

- **基础URL**: `http://localhost:8000`
- **认证方式**: Bearer Token (JWT)
- **响应格式**: JSON

## 认证端点

### 用户注册
```
POST /auth/register

请求体:
{
  "username": "string",
  "email": "string",
  "password": "string"
}

响应 (201):
{
  "id": 1,
  "username": "string",
  "email": "string",
  "balance": 1000.0,
  "is_active": true,
  "created_at": "2024-01-01T00:00:00"
}
```

### 用户登录
```
POST /auth/login

请求体:
{
  "username": "string",
  "password": "string"
}

响应 (200):
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "username": "string",
    "email": "string",
    "balance": 1000.0,
    "is_active": true,
    "created_at": "2024-01-01T00:00:00"
  }
}
```

## 比赛端点

### 创建比赛
```
POST /matches/

请求体:
{
  "title": "英超：曼联 vs 曼城",
  "team_a": "曼联",
  "team_b": "曼城",
  "odds_a": 2.5,
  "odds_b": 1.8,
  "odds_draw": 3.0,
  "start_time": "2024-01-15T15:00:00"
}

响应 (201):
{
  "id": 1,
  "title": "英超：曼联 vs 曼城",
  "team_a": "曼联",
  "team_b": "曼城",
  "odds_a": 2.5,
  "odds_b": 1.8,
  "odds_draw": 3.0,
  "status": "pending",
  "start_time": "2024-01-15T15:00:00",
  "end_time": null,
  "score_a": 0,
  "score_b": 0,
  "winner": null,
  "created_at": "2024-01-01T00:00:00"
}
```

### 获取所有比赛
```
GET /matches/?status=pending

参数:
- status (optional): pending, live, finished, cancelled

响应 (200):
[
  {
    "id": 1,
    "title": "...",
    ...
  }
]
```

### 获取比赛详情
```
GET /matches/{match_id}

响应 (200):
{
  "id": 1,
  "title": "...",
  ...
}
```

### 更新比赛
```
PUT /matches/{match_id}

请求体:
{
  "score_a": 2,
  "score_b": 1,
  "winner": "A",
  "status": "finished"
}

响应 (200):
{
  "id": 1,
  "title": "...",
  ...
}
```

## 下注端点

### 创建下注
```
POST /bets/?user_id=1

请求体:
{
  "match_id": 1,
  "choice": "A",
  "amount": 100.0
}

响应 (201):
{
  "id": 1,
  "user_id": 1,
  "match_id": 1,
  "choice": "A",
  "amount": 100.0,
  "odds": 2.5,
  "potential_payout": 250.0,
  "result": "pending",
  "winnings": 0.0,
  "created_at": "2024-01-01T00:00:00",
  "settled_at": null
}
```

### 获取用户下注
```
GET /bets/user/{user_id}

响应 (200):
[
  {
    "id": 1,
    "user_id": 1,
    ...
  }
]
```

### 获取下注详情
```
GET /bets/{bet_id}

响应 (200):
{
  "id": 1,
  ...
}
```

## 用户/钱包端点

### 获取用户信息
```
GET /users/{user_id}

响应 (200):
{
  "id": 1,
  "username": "string",
  "email": "string",
  "balance": 1000.0,
  "is_active": true,
  "created_at": "2024-01-01T00:00:00"
}
```

### 获取钱包余额
```
GET /users/{user_id}/wallet

响应 (200):
{
  "balance": 1000.0
}
```

### 存款
```
POST /users/{user_id}/deposit?amount=500

响应 (200):
{
  "balance": 1500.0,
  "amount": 500.0
}
```

### 提现
```
POST /users/{user_id}/withdraw?amount=200

响应 (200):
{
  "balance": 1300.0,
  "amount": 200.0
}
```

### 获取交易记录
```
GET /users/{user_id}/transactions

响应 (200):
[
  {
    "id": 1,
    "user_id": 1,
    "type": "deposit",
    "amount": 500.0,
    "description": "存款",
    "balance_after": 1500.0,
    "created_at": "2024-01-01T00:00:00"
  }
]
```

## 错误响应

```
{
  "detail": "错误描述信息"
}
```

### 常见状态码
- 200: 成功
- 201: 创建成功
- 400: 请求错误
- 401: 未授权
- 404: 资源不存在
- 500: 服务器错误

## 数据类型

### 下注选择
- "A": A队获胜
- "B": B队获胜
- "draw": 平局

### 下注状态
- "pending": 待结算
- "won": 赢了
- "lost": 输了

### 比赛状态
- "pending": 待开始
- "live": 进行中
- "finished": 已结束
- "cancelled": 已取消

### 交易类型
- "deposit": 存款
- "withdrawal": 提现
- "bet": 下注
- "payout": 赢利
