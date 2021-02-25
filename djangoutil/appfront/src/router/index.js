import Vue from 'vue'
import Router from 'vue-router'
import FundInfo from '../components/FundInfo'
import RandomImage from '../components/RandomImage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index'
    }, {
      path: '/fundInfo',
      name: 'FundInfo',
      component: FundInfo
    }, {
      path: '/randomimage',
      name: 'RandomImage',
      component: RandomImage
    }
  ]
})
