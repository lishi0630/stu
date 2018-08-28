import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import  "@/assets/js/rem.js"
import  "@/assets/js/ajax.js"

Vue.directive('focus', {
  update: function (a,b) {
    a.focus()
  },
})
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
