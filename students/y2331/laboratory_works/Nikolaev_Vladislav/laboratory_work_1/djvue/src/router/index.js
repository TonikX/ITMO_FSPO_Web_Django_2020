import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import Login from "../components/Login";
import Race from "../components/Race";
import Bus from "../components/Bus";
import Route from "../components/Route";
import Drivers from "../components/Drivers";
import Profile from "../components/Profile";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/buses',
      name: 'Bus',
      component: Bus
    },
    {
      path: '/races',
      name: 'Race',
      component: Race
    },
    {
      path: '/routes',
      name: 'Route',
      component: Route
    },
    {
      path: '/drivers',
      name: 'Drivers',
      component: Drivers
    },
    {
      path: '/profiles',
      name: 'Profile',
      component: Profile
    }

  ]
})
