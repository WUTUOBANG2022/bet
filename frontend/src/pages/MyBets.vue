<template>
  <div class="my-bets">
    <h1>🎲 我的下注</h1>
    
    <div class="filter-tabs">
      <button 
        v-for="tab in tabs" 
        :key="tab" 
        @click="activeTab = tab"
        :class="{ active: activeTab === tab }"
        class="tab"
      >
        {{ getTabLabel(tab) }}
      </button>
    </div>
    
    <div v-if="loading" class="loading">加载中...</div>
    
    <div v-if="!loading && filteredBets.length === 0" class="empty-state">
      暂无下注记录
    </div>
    
    <div v-if="!loading && filteredBets.length > 0" class="bets-list">
      <div v-for="bet in filteredBets" :key="bet.id" class="bet-item" :class="bet.result">
        <div class="bet-header">
          <span class="match-title">比赛 #{{ bet.match_id }}</span>
          <span class="status" :class="bet.result">{{ getResultLabel(bet.result) }}</span>
        </div>
        
        <div class="bet-details">
          <div class="detail">
            <span class="label">选择:</span>
            <span class="value">{{ bet.choice }}</span>
          </div>
          <div class="detail">
            <span class="label">下注金额:</span>
            <span class="value">￥{{ bet.amount.toFixed(2) }}</span>
          </div>
          <div class="detail">
            <span class="label">赔率:</span>
            <span class="value">{{ bet.odds }}</span>
          </div>
          <div class="detail">
            <span class="label">潜在收益:</span>
            <span class="value">￥{{ bet.potential_payout.toFixed(2) }}</span>
          </div>
          
          <div v-if="bet.result === 'won'" class="detail winning">
            <span class="label">实际赢利:</span>
            <span class="value">+￥{{ bet.winnings.toFixed(2) }}</span>
          </div>
        </div>
        
        <div class="bet-time">
          {{ formatTime(bet.created_at) }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      bets: [],
      loading: false,
      activeTab: 'all',
      tabs: ['all', 'pending', 'won', 'lost']
    }
  },
  computed: {
    filteredBets() {
      if (this.activeTab === 'all') return this.bets
      return this.bets.filter(b => b.result === this.activeTab)
    }
  },
  mounted() {
    this.loadBets()
  },
  methods: {
    async loadBets() {
      this.loading = true
      try {
        const user = JSON.parse(localStorage.getItem('user'))
        const response = await this.$http.get(`/bets/user/${user.id}`)
        this.bets = response.data.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
      } catch (err) {
        console.error('加载下注记录失败:', err)
      } finally {
        this.loading = false
      }
    },
    getResultLabel(result) {
      const labels = {
        'pending': '待结算',
        'won': '✅ 赢了',
        'lost': '❌ 输了'
      }
      return labels[result] || result
    },
    getTabLabel(tab) {
      const labels = {
        'all': '全部',
        'pending': '待结算',
        'won': '赢利',
        'lost': '亏损'
      }
      return labels[tab] || tab
    },
    formatTime(time) {
      const date = new Date(time)
      return date.toLocaleString('zh-CN')
    }
  }
}
</script>

<style scoped>
.my-bets {
  color: white;
}

.my-bets h1 {
  margin-bottom: 2rem;
}

.filter-tabs {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.tab {
  padding: 0.75rem 1.5rem;
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
}

.tab:hover {
  background: rgba(255, 255, 255, 0.2);
}

.tab.active {
  background: #ffd700;
  color: #333;
  border-color: #ffd700;
}

.loading, .empty-state {
  text-align: center;
  padding: 2rem;
}

.bets-list {
  display: grid;
  gap: 1rem;
}

.bet-item {
  background: rgba(255, 255, 255, 0.1);
  padding: 1.5rem;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-left: 4px solid rgba(255, 215, 0, 0.5);
}

.bet-item.won {
  border-left-color: #51cf66;
}

.bet-item.lost {
  border-left-color: #ff6b6b;
}

.bet-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.match-title {
  font-weight: bold;
  opacity: 0.9;
}

.status {
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  background: rgba(255, 215, 0, 0.2);
}

.status.pending {
  background: rgba(102, 126, 234, 0.2);
}

.status.won {
  background: rgba(81, 207, 102, 0.2);
  color: #51cf66;
}

.status.lost {
  background: rgba(255, 107, 107, 0.2);
  color: #ff6b6b;
}

.bet-details {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 1rem;
}

.detail {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.label {
  opacity: 0.7;
}

.value {
  font-weight: bold;
}

.detail.winning {
  grid-column: 1 / -1;
  color: #51cf66;
}

.bet-time {
  font-size: 0.8rem;
  opacity: 0.6;
}
</style>
