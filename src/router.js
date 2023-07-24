import { createRouter, createWebHistory } from 'vue-router'
import Setting from './components/setting.vue'
import FirstTimer from './components/FirstTimer.vue'
import StretchTime from './components/StretchTime.vue'
import FeedBack from './components/FeedBack.vue'

const routes = [
    {
        path: '/',
        redirect: '/setting'
    },
    {
        path: '/setting',
        component: Setting,
        props: true
    },
    {
        path: '/firsttimer',
        component: FirstTimer
    },
    {
        path: '/stretch',
        component: StretchTime
    },
    {
        path: '/feedback',
        component: FeedBack
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router

