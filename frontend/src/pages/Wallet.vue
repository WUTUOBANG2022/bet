<template>
  <div class="wallet-page">
    <h1>💳 我的钱包</h1>
    
    <div class="balance-card">
      <h2>账户余额</h2>
      <p class="balance">￥{{ balance }}</p>
    </div>
    
    <div class="actions">
      <div class="action-group">
        <h3>存款</h3>
        <div class="form-group">
          <input v-model.number="depositAmount" type="number" min="1" placeholder="输入存款金额">
          <button @click="deposit" class="action-btn">存款</button>
        </div>
      </div>
      
      <div class="action-group">
        <h3>提现</h3>
        <div class="form-group">
          <input v-model.number="withdrawAmount" type="number" min="1" placeholder="输入提现金额">
          <button @click="withdraw" class="action-btn">提现</button>
        </div>
      </div>
    </div>
    
    <div class="transactions">
      <h3>交易记录</h3>
      <div v-if="transactionList.length === 0" class="empty-state">
        暂无交易记录
      </div>
      <table v-if="transactionList.length > 0">
        <thead>
          <tr>
            <th>交易类型</th>
            <th>金额</th>
            <th>余额</th>
            <th>时间</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="t in transactionList" :key="t.id" :class="t.type">
            <td>{{ getTypeLabel(t.type) }}</td>
            <td>{{ t.type === 'deposit' || t.type === 'payout' ? '+' : '-' }}￥{{ t.amount.toFixed(2) }}</td>
            <td>￥{{ t.balance_after.toFixed(2) }}</td>
            <td>{{ formatTime(t.created_at) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      balance: 0,
      depositAmount: 0,
      withdrawAmount: 0,
      transactionList: []
    }
  },
  mounted() {
    this.loadWalletData()
  },
  methods: {
    async loadWalletData() {
      try {
        const user = JSON.parse(localStorage.getItem('user'))
        const response = await this.$http.get(`/users/${user.id}`)
        this.balance = response.data.balance.toFixed(2)
        
        const transRes = await this.$http.get(`/users/${user.id}/transactions`)
        this.transactionList = transRes.data
      } catch (err) {
        console.error('加载钱包数据失败:', err)
      }
    },
    async deposit() {
      if (this.depositAmount <= 0) {
        alert('请输入有效的金额')
        return
      }
      
      try {
        const user = JSON.parse(localStorage.getItem('user'))
        await this.$http.post(`/users/${user.id}/deposit?amount=${this.depositAmount}`)
        this.depositAmount = 0
        this.loadWalletData()
        alert('存款成功！')
      } catch (err) {
        alert(err.response?.data?.detail || '存款失败')
      }
    },
    async withdraw() {
      if (this.withdrawAmount <= 0) {
        alert('请输入有效的金额')
        return
      }
      
      try {
        const user = JSON.parse(localStorage.getItem('user'))
        await this.$http.post(`/users/${user.id}/withdraw?amount=${this.withdrawAmount}`)
        this.withdrawAmount = 0
        this.loadWalletData()
        alert('提现成功！')
      } catch (err) {
        alert(err.response?.data?.detail || '提现失败')
      }
    },
    getTypeLabel(type) {
      const labels = {
        'deposit': '存款',
        'withdrawal': '提现',
        'bet': '下注',
        'payout': '赢利'
      }
      return labels[type] || type
    },
    formatTime(time) {
      const date = new Date(time)
      return date.toLocaleString('zh-CN')
    }
  }
}
</script>

<style scoped>
.wallet-page {
  color: white;
}

.wallet-page h1 {
  margin-bottom: 2rem;
}

.balance-card {
  background: rgba(255, 215, 0, 0.2);
  padding: 2rem;
  border-radius: 10px;
  margin-bottom: 2rem;
  border: 2px solid rgba(255, 215, 0, 0.5);
}

.balance-card h2 {
  margin-bottom: 1rem;
}

.balance {
  font-size: 2.5rem;
  font-weight: bold;
  color: #ffd700;
}

.actions {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.action-group {
  background: rgba(255, 255, 255, 0.1);
  padding: 1.5rem;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.action-group h3 {
  margin-bottom: 1rem;
}

.form-group {
  display: flex;
  gap: 0.5rem;
}

.form-group input {
  flex: 1;
  padding: 0.75rem;
  border: none;
  border-radius: 5px;
}

.action-btn {
  padding: 0.75rem 1.5rem;
  background: #ffd700;
  color: #333;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: 0.3s;
}

.action-btn:hover {
  background: #ffed4e;
}

.transactions {
  background: rgba(255, 255, 255, 0.1);
  padding: 1.5rem;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.transactions h3 {
  margin-bottom: 1rem;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 0.75rem;
  text-align: left;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

th {
  font-weight: bold;
}

tr.deposit td:nth-child(2) {
  color: #51cf66;
}

tr.withdrawal td:nth-child(2) {
  color: #ff6b6b;
}

tr.payout td:nth-child(2) {
  color: #51cf66;
}

.empty-state {
  text-align: center;
  padding: 2rem;
  opacity: 0.7;
}
</style>
