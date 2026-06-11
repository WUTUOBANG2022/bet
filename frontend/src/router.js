import { createRouter, createWebHistory } from 'vue-router'
import Login from './pages/Login.vue'
import Register from './pages/Register.vue'
import Matches from './pages/Matches.vue'
import Dashboard from './pages/Dashboard.vue'
import Wallet from './pages/Wallet.vue'
import MyBets from './pages/MyBets.vue'

const routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/matches', component: Matches, meta: { requiresAuth: true } },
  { path: '/wallet', component: Wallet, meta: { requiresAuth: true } },
  { path: '/my-bets', component: MyBets, meta: { requiresAuth: true } }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access_token')
  
  if (to.meta.requiresAuth && !token) {
    next('/login')
  } else if ((to.path === '/login' || to.path === '/register') && token) {
    next('/dashboard')
  } else {
    next()
  }
})

export default router
