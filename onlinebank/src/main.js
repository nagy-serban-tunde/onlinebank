import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import '@fortawesome/fontawesome-free/css/all.css'

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(Vuex)

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
