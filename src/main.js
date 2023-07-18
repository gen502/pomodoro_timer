import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from './App.vue'
import router from './router'

// ストアを作成
const store = createStore({
    state: {
        workTime: 0,
        breakTime: 0,
        setCount: 0,
    },
    mutations: {
        setWorkTime(state, value) {
            state.workTime = value;
        },
        setBreakTime(state, value) {
            state.breakTime = value;
        },
        setSetCount(state, value) {
            state.setCount = value;
        },
    },
})

createApp(App).use(store).use(router).mount('#app')
