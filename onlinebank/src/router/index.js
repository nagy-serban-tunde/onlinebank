import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home.vue'

Vue.use(VueRouter)

// Define some routes
const routes = [
  { path: "/home", component: Home },
  { path: "/", component: Home }
]

// Create the router instance and pass the `routes` option
const router = new VueRouter({
  routes,
  mode:"history",
});

// Exporting "router" so it can be seen by others
export default router