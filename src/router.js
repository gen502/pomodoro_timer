import { createRouter, createWebHistory } from 'vue-router'
import Setting from './components/setting.vue'
import FirstTimer from './components/FirstTimer.vue'

const routes = [
    {
        path: '/',
        redirect: '/setting'
    },
    {
        path: '/setting',
        component: Setting
    },
    {
        path: '/firsttimer',
        component: FirstTimer
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router

