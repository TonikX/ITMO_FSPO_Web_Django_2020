import Vue from 'vue';
import Vuetify from 'vuetify/es5';

Vue.use(Vuetify);

const user = JSON.parse(localStorage.getItem('vuetify@user') || "{}");

export default new Vuetify(user || {});
