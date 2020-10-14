import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Register from '@/components/Register'
import EditUser from '@/components/EditUser'
import Main from '@/components/Main'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Main
    }, {
      path: '/login',
      name: 'login',
      component: Login
    }, {
      path: '/reg',
      name: 'register',
      component: Register
    }, {
      path: '/edit',
      name: 'edit',
      component: EditUser
    },
  ]
})
