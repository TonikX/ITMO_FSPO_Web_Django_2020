import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Login from '../components/Login.vue'
import SignUp from "../components/SignUp.vue";
import ExamSchedule from "../components/ExamSchedule.vue";
import Student from "../components/Student.vue";
import Discipline from "../components/Discipline.vue";
import Teacher from "../components/Teacher.vue";
import Exam from "../components/Exam.vue";


import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';

Vue.use(MuseUI);
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUp
  },
  {
    path: '/schedule',
    name: 'schedule',
    component: ExamSchedule
  },
  {
    path: '/student',
    name: 'student',
    component: Student
  },
  {
    path: '/discipline',
    name: 'discipline',
    component: Discipline
  },
  {
    path: '/teacher',
    name: 'teacher',
    component: Teacher
  },
  {
    path: '/exam',
    name: 'exam',
    component: Exam
  },
]

const router = new VueRouter({
  routes
})

export default router
