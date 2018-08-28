import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import register from './views/register'
import amend from "./views/amend"
import password from "./views/password"
import details from "./views/details"
import catalong from "./views/catalong"

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      // beforeEnter(to,from,next){
      //    if(!sessionStorage["names"]){
      //        next("/home")
      //    }else{
      //        next();
      //    }
      // },
    },
      {
      path: '/register',
      name: 'register',
      component: register
    },
       {
      path: '/amend',
      name: 'amend',
      component: amend
    },
      {
      path: '/password/:uid',
      name: 'password',
      component: password
    },
      {
      path: '/details',
      name: 'details',
      component: details
    },
       {
      path: '/catalong',
      name: 'catalong',
      component: catalong
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component:() => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
// export default router
