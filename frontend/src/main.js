import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

const app = createApp(App)

// 配置axios
axios.defaults.baseURL = 'http://localhost:8000'
app.config.globalProperties.$http = axios

// 从localStorage获取token并设置到请求头
const token = localStorage.getItem('access_token')
if (token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
}

app.use(router)
app.mount('#app')
