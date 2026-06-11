<template>
  <div class="matches-page">
    <h1>⚽ 比赛列表</h1>
    
    <div v-if="loading" class="loading">加载中...</div>
    
    <div v-if="!loading && matches.length === 0" class="empty-state">
      暂无比赛
    </div>
    
    <div v-if="!loading && matches.length > 0" class="matches-grid">
      <div v-for="match in matches" :key="match.id" class="match-card">
        <div class="match-header">
          <span class="status" :class="match.status">{{ match.status }}</span>
          <span class="time">{{ formatTime(match.start_time) }}</span>
        </div>
        
        <div class="match-teams">
          <div class="team">
            <div class="team-name">{{ match.team_a }}</div>
            <div class="odds">{{ match.odds_a }}</div>
          </div>
          <div class="vs">VS</div>
          <div class="team">
            <div class="team-name">{{ match.team_b }}</div>
            <div class="odds">{{ match.odds_b }}</div>
          </div>
        </div>
        
        <div class="draw-odds">
          <span>平</span>
          <span>{{ match.odds_draw }}</span>
        </div>
        
        <div class="bet-actions">
          <button @click="selectBet(match, 'A')" class="bet-btn">下注{{ match.team_a }}</button>
          <button @click="selectBet(match, 'draw')" class="bet-btn draw">平局</button>
          <button @click="selectBet(match, 'B')" class="bet-btn">下注{{ match.team_b }}</button>
        </div>
      </div>
    </div>
    
    <!-- 下注模态框 -->
    <div v-if="showBetModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="showBetModal = false">&times;</span>
        <h2>下注确认</h2>
        <p>{{ selectedMatch?.title }}</p>
        <p>选择: {{ selectedChoice === 'A' ? selectedMatch?.team_a : selectedChoice === 'B' ? selectedMatch?.team_b : '平局' }}</p>
        <p>赔率: {{ getOdds() }}</p>
        
        <div class="form-group">
          <label>下注金额 (￥)</label>
          <input v-model.number="betAmount" type="number" min="1" placeholder="输入金额">
        </div>
        
        <p v-if="betAmount > 0" class="potential">
          潜在收益: ￥{{ (betAmount * getOdds()).toFixed(2) }}
        </p>
        
        <button @click="placeBet" class="confirm-btn">确认下注</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      matches: [],
      loading: false,
      showBetModal: false,
      selectedMatch: null,
      selectedChoice: null,
      betAmount: 0
    }
  },
  mounted() {
    this.loadMatches()
  },
  methods: {
    async loadMatches() {
      this.loading = true
      try {
        const response = await this.$http.get('/matches')
        this.matches = response.data
      } catch (err) {
        console.error('加载比赛失败:', err)
      } finally {
        this.loading = false
      }
    },
    selectBet(match, choice) {
      this.selectedMatch = match
      this.selectedChoice = choice
      this.showBetModal = true
      this.betAmount = 0
    },
    getOdds() {
      if (!this.selectedMatch) return 0
      if (this.selectedChoice === 'A') return this.selectedMatch.odds_a
      if (this.selectedChoice === 'B') return this.selectedMatch.odds_b
      return this.selectedMatch.odds_draw
    },
    async placeBet() {
      if (this.betAmount <= 0) {
        alert('请输入有效的金额')
        return
      }
      
      try {
        const user = JSON.parse(localStorage.getItem('user'))
        const response = await this.$http.post('/bets/', {
          match_id: this.selectedMatch.id,
          choice: this.selectedChoice,
          amount: this.betAmount
        }, {
          params: { user_id: user.id }
        })
        
        alert('下注成功！')
        this.showBetModal = false
        this.loadMatches()
      } catch (err) {
        alert(err.response?.data?.detail || '下注失败')
      }
    },
    formatTime(time) {
      const date = new Date(time)
      return date.toLocaleString('zh-CN')
    }
  }
}
</script>

<style scoped>
.matches-page {
  color: white;
}

.matches-page h1 {
  margin-bottom: 2rem;
}

.loading, .empty-state {
  text-align: center;
  padding: 2rem;
  font-size: 1.1rem;
}

.matches-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

.match-card {
  background: rgba(255, 255, 255, 0.1);
  padding: 1.5rem;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.match-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.status {
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  background: rgba(255, 215, 0, 0.2);
}

.status.live {
  background: rgba(255, 107, 107, 0.2);
}

.match-teams {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  gap: 1rem;
}

.team {
  flex: 1;
  text-align: center;
}

.team-name {
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.odds {
  background: rgba(255, 255, 255, 0.2);
  padding: 0.5rem;
  border-radius: 5px;
  font-size: 1.2rem;
}

.vs {
  opacity: 0.7;
}

.draw-odds {
  text-align: center;
  margin-bottom: 1rem;
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.draw-odds span:last-child {
  background: rgba(255, 255, 255, 0.2);
  padding: 0.25rem 1rem;
  border-radius: 5px;
}

.bet-actions {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
}

.bet-btn {
  padding: 0.75rem;
  background: rgba(255, 215, 0, 0.8);
  color: #333;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
  font-weight: bold;
}

.bet-btn:hover {
  background: #ffd700;
}

.bet-btn.draw {
  background: rgba(102, 126, 234, 0.8);
  color: white;
}

.bet-btn.draw:hover {
  background: #667eea;
}

.modal {
  display: flex;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  max-width: 500px;
  width: 90%;
  color: #333;
}

.close {
  float: right;
  font-size: 2rem;
  font-weight: bold;
  cursor: pointer;
}

.form-group {
  margin: 1rem 0;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
}

.form-group input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.potential {
  color: #667eea;
  font-weight: bold;
  margin: 1rem 0;
}

.confirm-btn {
  width: 100%;
  padding: 0.75rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
}

.confirm-btn:hover {
  background: #764ba2;
}
</style>
