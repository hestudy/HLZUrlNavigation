import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';
import axios from 'axios'
import vuecookie from 'vue-cookie'
import Vant from 'vant';
import 'vant/lib/index.css';

Vue.use(Vant);
Vue.use(vuecookie)
axios.defaults.withCredentials=true
Vue.prototype.$axios = axios;
Vue.use(ViewUI)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
