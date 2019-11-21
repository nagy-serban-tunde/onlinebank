import Vue from 'vue'
import VueRouter from 'vue-router'
import Root from '@/components/Root.vue'
import Home from '@/components/Home.vue'
import Statistics from '@/components/Statistics.vue'
import Account from '@/components/Account.vue'
import Register from '@/components/Register.vue'
import Login from '@/components/Login.vue'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: "/", component: Root,
      children: [
        { path: '', redirect: { name: 'Login' } },
        { path: 'home', name: 'Home', component: Home },
        { path: 'statistics', name: 'Statistics', component: Statistics },
        { path: 'account', name: 'Account', component: Account }
      ]
    },
    { path: '/register', name: 'Register', component: Register },
    { path: '/login', name: 'Login', component: Login }
  ]
})
