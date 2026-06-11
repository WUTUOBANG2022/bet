<template>
  <div class="register-page">
    <div class="register-card">
      <h1>🎲 创建账户</h1>
      <form @submit.prevent="register">
        <div class="form-group">
          <label>用户名</label>
          <input v-model="form.username" type="text" placeholder="输入用户名" required>
        </div>
        <div class="form-group">
          <label>邮箱</label>
          <input v-model="form.email" type="email" placeholder="输入邮箱" required>
        </div>
        <div class="form-group">
          <label>密码</label>
          <input v-model="form.password" type="password" placeholder="输入密码" required>
        </div>
        <button type="submit" class="submit-btn" :disabled="loading">
          {{ loading ? '注册中...' : '注册' }}
        </button>
      </form>
      <p class="switch-text">
        已有账户？<router-link to="/login">立即登录</router-link>
      </p>
      <div v-if="error" class="error-message">{{ error }}</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: '',
        email: '',
        password: ''
      },
      loading: false,
      error: ''
    }
  },
  methods: {
    async register() {
      this.loading = true
      this.error = ''
      try {
        await this.$http.post('/auth/register', this.form)
        this.$router.push('/login')
      } catch (err) {
        this.error = err.response?.data?.detail || '注册失败'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.register-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.register-card {
  background: white;
  padding: 3rem;
  border-radius: 10px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 400px;
}

.register-card h1 {
  text-align: center;
  margin-bottom: 2rem;
  color: #333;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #333;
}

.form-group input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
}

.submit-btn {
  width: 100%;
  padding: 0.75rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: 0.3s;
}

.submit-btn:hover:not(:disabled) {
  opacity: 0.9;
}

.submit-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.switch-text {
  text-align: center;
  margin-top: 1rem;
  color: #666;
}

.switch-text a {
  color: #667eea;
  text-decoration: none;
  font-weight: bold;
}

.error-message {
  color: #ff6b6b;
  margin-top: 1rem;
  padding: 0.75rem;
  background: #ffe0e0;
  border-radius: 5px;
  text-align: center;
}
</style>
