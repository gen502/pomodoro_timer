<template>
  <!-- 最上位のrouter-viewにv-bind:classを追加して、動的にクラスを適用 -->
  <router-view :class="{ 'minimized-size': isTimerMinimized }" />
</template>

<script>
export default {
  name: 'App',
  computed: {
    isTimerMinimized() {
      return this.$route.path === '/firsttimer' && this.$store.state.isMinimized;
    }
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

.minimized-size {
  transform: scale(0.5);
}
</style>
