// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router'
import vuetify from './plugins/vuetify';
import VuetifyNumberInput from '@jzolago/vuetify-number-input'
import './assets/main.css'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import '@mdi/font/css/materialdesignicons.css'

Array.prototype.insert = function (i, e) { this.splice(i, 0, e); }
String.prototype.beautify = function() {
  return this.replace(/([A-Z]+)/g, " $1").replace(/([A-Z][a-z])/g, " $1").trim();
}
Vue.config.productionTip = false;
Vue.prototype.$forceCompute= function(computedName, forceUpdate /* default: true */) {
	if (this._computedWatchers[computedName]) {
		this._computedWatchers[computedName].run();
		if (forceUpdate || typeof forceUpdate == 'undefined') this.$forceUpdate()
	}
}
Vue.use(VueAxios, axios);
Vue.use(VuetifyNumberInput);
((v) => {
  function plugin(Vue, obj) {
    if (plugin.installed) {
      return
    }
    plugin.installed = true
  
    if (!obj) {
      console.error('You have to install axios')
      return
    }

    Vue.$me = obj
  
    Object.defineProperties(Vue.prototype, {
  
      $me: {
        get() {
          return obj
        }
      },
    })
  }

  var obj = {};
  v.use(plugin, obj);
})(Vue);
Vue.$me.host = document.location.hostname + ":8000";
Vue.$me.settings = {
  self: JSON.parse(localStorage.getItem('vuetify@user') || "{\"theme\":{}}"),
  save: () => {
    localStorage.setItem('vuetify@user', JSON.stringify(Vue.$me.settings.self));
  }
}
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  vuetify,
  template: '<App/>'
})