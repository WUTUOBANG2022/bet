<template>
  <div class="dashboard">
    <h1>📊 仪表盘</h1>
    <div class="stats-grid">
      <div class="stat-card">
        <h3>💰 账户余额</h3>
        <p class="stat-value">{{ userBalance }}</p>
      </div>
      <div class="stat-card">
        <h3>🎯 活跃下注</h3>
        <p class="stat-value">{{ activeBets }}</p>
      </div>
      <div class="stat-card">
        <h3>✅ 赢利</h3>
        <p class="stat-value">{{ totalWinnings }}</p>
      </div>
      <div class="stat-card">
        <h3>📈 比赛总数</h3>
        <p class="stat-value">{{ totalMatches }}</p>
      </div>
    </div>
    
    <div class="actions">
      <router-link to="/matches" class="action-btn primary">📌 查看比赛</router-link>
      <router-link to="/my-bets" class="action-btn">🎲 我的下注</router-link>
      <router-link to="/wallet" class="action-btn">💳 钱包</router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userBalance: 0,
      activeBets: 0,
      totalWinnings: 0,
      totalMatches: 0
    }
  },
  mounted() {
    this.loadDashboardData()
  },
  methods: {
    async loadDashboardData() {
      try {
        const user = JSON.parse(localStorage.getItem('user'))
        if (user) {
          this.userBalance = '￥' + user.balance.toFixed(2)
        }
        
        // 获取比赛数量
        const matchesRes = await this.$http.get('/matches')
        this.totalMatches = matchesRes.data.length
        
        // 获取用户的下注
        const betsRes = await this.$http.get(`/bets/user/${user.id}`)
        this.activeBets = betsRes.data.filter(b => b.result === 'pending').length
        this.totalWinnings = betsRes.data
          .filter(b => b.result === 'won')
          .reduce((sum, b) => sum + b.winnings, 0)
          .toFixed(2)
      } catch (err) {
        console.error('加载数据失败:', err)
      }
    }
  }
}
</script>

<style scoped>
.dashboard {
  color: white;
}

.dashboard h1 {
  margin-bottom: 2rem;
  font-size: 2rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: rgba(255, 255, 255, 0.1);
  padding: 2rem;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.stat-card h3 {
  font-size: 0.9rem;
  margin-bottom: 1rem;
  opacity: 0.9;
}

.stat-value {
  font-size: 2rem;
  font-weight: bold;
}

.actions {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.action-btn {
  padding: 1rem;
  text-align: center;
  text-decoration: none;
  background: rgba(255, 255, 255, 0.2);
  color: white;
  border-radius: 5px;
  transition: 0.3s;
  cursor: pointer;
  border: none;
  font-size: 1rem;
}

.action-btn:hover {
  background: rgba(255, 255, 255, 0.3);
}

.action-btn.primary {
  background: #ffd700;
  color: #333;
}

.action-btn.primary:hover {
  background: #ffed4e;
}
</style>
