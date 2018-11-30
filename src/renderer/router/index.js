import Vue from 'vue'
import Router from 'vue-router'
// import Welcome from '@/pages/welcome/Welcome'
import IPhone from '@/pages/iphone/IPhone'
import Wechat from '@/pages/iphone/Wechat'
import Screen from '@/pages/iphone/Screen'
// import Home from '@/pages/home/Home'
import Creative from '@/pages/creative/Creative'

Vue.use(Router)

export default new Router({
  // mode: 'history',
  routes: [
    {
      path: '/iphone',
      name: 'IPhone',
      component: IPhone,
      children: [
        {
          path: 'wechat',
          name: 'Wechat',
          component: Wechat
        },
        {
          path: 'screen',
          name: 'Screen',
          component: Screen
        }
      ]

    }, {
      path: '/creative',
      component: Creative,
      children: []
    }, {
      path: '*',
      redirect: '/creative'
    }
  ]
})
