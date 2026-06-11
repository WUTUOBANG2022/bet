<template>
  <div class="app-container">
    <nav class="navbar" v-if="isLoggedIn">
      <div class="nav-logo">🎲 BET系统</div>
      <div class="nav-links">
        <router-link to="/dashboard" class="nav-link">仪表盘</router-link>
        <router-link to="/matches" class="nav-link">比赛</router-link>
        <router-link to="/my-bets" class="nav-link">我的下注</router-link>
        <router-link to="/wallet" class="nav-link">钱包</router-link>
        <button class="logout-btn" @click="logout">登出</button>
      </div>
    </nav>
    
    <div class="main-content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    isLoggedIn() {
      return localStorage.getItem('access_token') !== null
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('access_token')
      localStorage.removeItem('user')
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.app-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(0, 0, 0, 0.3);
  padding: 1rem 2rem;
  color: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.nav-logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-links {
  display: flex;
  gap: 1.5rem;
  align-items: center;
}

.nav-link {
  color: white;
  text-decoration: none;
  transition: 0.3s;
}

.nav-link:hover {
  color: #ffd700;
}

.logout-btn {
  background: #ff6b6b;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
}

.logout-btn:hover {
  background: #ff5252;
}

.main-content {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}
</style>
