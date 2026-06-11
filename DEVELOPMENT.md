# 开发指南

## 项目架构

### 三层架构

```
┌─────────────────────────────────┐
│        前端 (Vue.js)             │
│   Pages, Components, Router      │
└────────────────┬──────────────────┘
                 │ HTTP/JSON
┌────────────────▼──────────────────┐
│      后端 API (FastAPI)           │
│   Routes, Models, Schemas         │
└────────────────┬──────────────────┘
                 │ SQL
┌────────────────▼──────────────────┐
│      数据库 (SQLite)              │
│   Users, Matches, Bets, Txns      │
└─────────────────────────────────┘
```

## 后端开发

### 目录结构
```
backend/app/
├── models/           # SQLAlchemy ORM模型
│   ├── user.py       # 用户模型
│   ├── match.py      # 比赛模型
│   ├── bet.py        # 下注模型
│   └── transaction.py # 交易模型
├── routes/           # API路由
│   ├── auth.py       # 认证相关API
│   ├── matches.py    # 比赛相关API
│   ├── bets.py       # 下注相关API
│   └── users.py      # 用户相关API
├── auth.py           # 认证和密码管理
├── schemas.py        # Pydantic数据验证模型
├── config.py         # 配置管理
├── database.py       # 数据库连接
└── main.py           # FastAPI应用入口
```

### 添加新的API端点

1. **创建数据模型** (models/):
```python
from sqlalchemy import Column, Integer, String
from app.database import Base

class Example(Base):
    __tablename__ = "examples"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
```

2. **创建数据验证Schema** (schemas.py):
```python
from pydantic import BaseModel

class ExampleCreate(BaseModel):
    name: str

class ExampleResponse(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True
```

3. **创建API路由** (routes/examples.py):
```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Example
from app.schemas import ExampleCreate, ExampleResponse

router = APIRouter(prefix="/examples", tags=["examples"])

@router.post("/", response_model=ExampleResponse)
def create_example(item: ExampleCreate, db: Session = Depends(get_db)):
    db_item = Example(name=item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
```

4. **注册路由** (main.py):
```python
from app.routes import example_router

app.include_router(example_router)
```

### 数据库操作

#### 创建记录
```python
user = User(username="john", email="john@example.com")
db.add(user)
db.commit()
```

#### 查询记录
```python
# 按ID查询
user = db.query(User).filter(User.id == 1).first()

# 条件查询
users = db.query(User).filter(User.is_active == True).all()

# 排序和限制
users = db.query(User).order_by(User.created_at.desc()).limit(10).all()
```

#### 更新记录
```python
user = db.query(User).filter(User.id == 1).first()
user.email = "newemail@example.com"
db.commit()
```

#### 删除记录
```python
user = db.query(User).filter(User.id == 1).first()
db.delete(user)
db.commit()
```

## 前端开发

### Vue组件结构

```vue
<template>
  <!-- HTML -->
</template>

<script>
export default {
  name: 'ComponentName',
  data() {
    return {
      // 响应式数据
    }
  },
  computed: {
    // 计算属性
  },
  methods: {
    // 方法
  },
  mounted() {
    // 生命周期钩子
  }
}
</script>

<style scoped>
/* 组件样式 */
</style>
```

### 创建新页面

1. **创建页面组件** (src/pages/NewPage.vue)
2. **添加路由** (src/router.js):
```javascript
import NewPage from './pages/NewPage.vue'

const routes = [
  { path: '/new-page', component: NewPage, meta: { requiresAuth: true } }
]
```

### 调用API

```javascript
// 获取数据
async loadData() {
  try {
    const response = await this.$http.get('/endpoint')
    this.data = response.data
  } catch (error) {
    console.error('Error:', error)
  }
}

// 发送数据
async submitForm() {
  try {
    const response = await this.$http.post('/endpoint', this.form)
    console.log('Success:', response.data)
  } catch (error) {
    console.error('Error:', error)
  }
}
```

### 状态管理

如果需要全局状态，可以添加Pinia/Vuex:

```javascript
// 安装
npm install pinia

// 创建store
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    token: null
  }),
  getters: {
    isLoggedIn: (state) => state.token !== null
  },
  actions: {
    setUser(user) {
      this.user = user
    }
  }
})
```

## 测试

### 后端单元测试

```python
# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/auth/register",
        json={"username": "test", "email": "test@example.com", "password": "123456"}
    )
    assert response.status_code == 200
```

### 前端组件测试

```javascript
// 使用Vitest
import { test, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import MyComponent from './MyComponent.vue'

test('component renders properly', () => {
  const wrapper = mount(MyComponent)
  expect(wrapper.text()).toContain('Expected text')
})
```

## 调试

### 后端调试

```python
# 启用调试模式
app = FastAPI(debug=True)

# 打印调试信息
import logging
logger = logging.getLogger(__name__)
logger.debug("Debug message")
```

### 前端调试

```javascript
// 使用浏览器开发工具
console.log('Debug info:', data)

// Vue开发工具浏览器扩展
// 访问 http://localhost:8000/docs (Swagger UI)
```

## 代码规范

### Python (PEP 8)
```python
# 类命名：PascalCase
class UserModel:
    pass

# 函数命名：snake_case
def get_user(user_id):
    pass

# 常量命名：UPPER_SNAKE_CASE
MAX_RETRIES = 3
```

### JavaScript (ES6+)
```javascript
// 组件命名：PascalCase
export default {
  name: 'MyComponent'
}

// 函数命名：camelCase
function getUserData() {
  return {}
}

// 常量命名：UPPER_SNAKE_CASE
const MAX_RETRIES = 3
```

## 性能优化

### 后端优化
1. 数据库索引
2. 查询优化（避免N+1问题）
3. 缓存（Redis）
4. 异步处理（Celery）
5. 分页

### 前端优化
1. 代码分割
2. 组件懒加载
3. 图片优化
4. 缓存策略
5. 虚拟滚动

## 常见问题

### Q: 如何修改赔率？
A: 在 `models/match.py` 中修改默认值，或通过API动态更新。

### Q: 如何添加新的下注类型？
A: 修改 `Bet` 模型和相关API，支持多个下注选项。

### Q: 如何实现实时更新？
A: 集成WebSocket库（如 `python-socketio` 和 `socket.io-client`）。

### Q: 如何处理并发下注？
A: 使用数据库事务和锁机制确保数据一致性。

## 贡献指南

1. Fork项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 资源链接

- [FastAPI官方文档](https://fastapi.tiangolo.com/)
- [Vue 3官方文档](https://vuejs.org/)
- [SQLAlchemy官方文档](https://docs.sqlalchemy.org/)
- [Vite官方文档](https://vitejs.dev/)
