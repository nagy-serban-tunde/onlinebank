import Vue from 'vue'
import VueRouter from 'vue-router'
import Root from '@/components/Root.vue'
import Home from '@/components/Home.vue'
import Statistics from '@/components/Statistics.vue'
import Account from '@/components/Account.vue'

Vue.use(VueRouter)

// Define some routes
const routes = [
  {
    path: "/", component: Root, 
    children: [
      { path: '', redirect: { name: 'Home' }},
      { path: 'home', name: 'Home', component: Home },
      { path: 'statistics', name: 'Statistics', component: Statistics },
      { path: 'account', name: 'Account', component: Account },
    ]
  }
]

// Create the router instance and pass the `routes` option
const router = new VueRouter({
  routes,
  mode: "history",
});

// Exporting "router" so it can be seen by others
export default router