
<template>
  <setting />
</template>

<script>
import setting from './components/setting.vue'
import FeedBack from './components/FeedBack.vue'
import FirstTimer from './components/FirstTimer.vue'
import StretchTime from './components/StretchTime.vue'


export default {
  name: 'App',
  components: {
    setting,
    FeedBack,
    FirstTimer,
    StretchTime,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>