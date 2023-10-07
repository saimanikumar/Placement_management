import { createRouter, createWebHistory } from 'vue-router'

import StudentBoard from "../views/Boards/StudentBoard.vue"
import DeptBoard from "../views/Boards/DeptBoard.vue"
import AdminBoard from "../views/Boards/AdminBoard.vue"
import AddDetails from "../views/Boards/AddDetails.vue"
import Details from "../views/Boards/Details.vue"


import StudentLogin from "../views/Logins/StudentLogin.vue"
import AdminLogin from "../views/Logins/AdminLogin.vue"
import DeptLogin from "../views/Logins/DeptLogin.vue"

// import Summary from "../views/Summary.vue"
import Signup from "../views/Register.vue"
import Home from "../views/Home.vue"

// import TheatreForm from "../views/TheatreForm.vue"
// import ShowForm from "../views/ShowForm.vue"
// import Summary from "../views/Summary.vue"
// import BookingForm from "../views/BookingForm.vue"
// import Bookings from "../views/Bookings.vue"

import store from "../store";

function check_route_admin(to, from, next) {
  var isAuthenticated = false

  if (store.state.loggedIn)
      isAuthenticated = true
  else
      isAuthenticated = false
  
  if (isAuthenticated && store.state.role == 'admin') {
      next()
  }
  else {
      next('/')
  }
}

function check_route_user(to, from, next) {
  var isAuthenticated = false

  if (store.state.loggedIn)
      isAuthenticated = true
  else
      isAuthenticated = false
  
  if (isAuthenticated && store.state.role == 'student') {
      next()
  }
  else {

      next('/')
  }
}

function check_route_dept(to, from, next) {
  var isAuthenticated = false

  if (store.state.loggedIn)
      isAuthenticated = true
  else
      isAuthenticated = false
  
  if (isAuthenticated && store.state.role == 'dept') {
      next()
  }
  else {

      next('/')
  }
}

function clearToken(to, from, next) {
  localStorage.removeItem('token');
  next();
}
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),

  routes: [
    { path: '/stulogin', name: 'stulogin', component: StudentLogin },
    { path: '/admlogin', name: 'admlogin', component: AdminLogin },
    { path: '/deptlogin', name: 'deptlogin', component: DeptLogin },
    
    { path: '/studentboard/:id', name: 'student_board', component: StudentBoard, beforeEnter: check_route_user},
    { path: '/adminboard', name: 'admin_board', component: AdminBoard, beforeEnter: check_route_admin},
    { path: '/deptboard/:id', name: 'dept_board', component: DeptBoard, beforeEnter: check_route_dept},
    
    { path: '/addDetails', name: 'add_details', component: AddDetails, beforeEnter: check_route_admin},

    { path: '/admindetails', name: 'admin_details', component: Details, beforeEnter: check_route_admin},

    { path: '/register', name: 'register', component: Signup },
    { path: '/', name: 'home', component: Home },
    // { path: '/adsum', name: 'adsum', component: Summary },

    
    // { path: '/summary', name: 'summary', component: Summary, beforeEnter: check_route_admin},

    // { path: '/theatre/create', name: 'create_theatre', component: TheatreForm, beforeEnter: check_route_admin},
    // { path: '/theatre/update/:id', name: 'update_theatre', component: TheatreForm, beforeEnter: check_route_admin },
    
    // { path: '/show/create/:th_id', name: 'create_show', component: ShowForm, beforeEnter: check_route_admin },
    // { path: '/show/update/:th_id/:s_id', name: 'update_show', component: ShowForm, beforeEnter: check_route_admin },

    
    // { path: '/board/book/:th_id/:s_id', name: 'user_booking', component: BookingForm, beforeEnter: check_route_user},

    // { path: '/board/bookings', name: 'bookings', component: Bookings, beforeEnter: check_route_user},


    
  ]
})

export default router
