<!-- <template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Hello World!"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
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
</style> -->

<template>
  <div class="timer">
    <h1>{{ formatTime }}</h1>
    <button @click="startTimer" v-if="!timerRunning">Start</button>
    <button @click="stopTimer" v-if="timerRunning">Stop</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      timerRunning: false,
      timeLeft: 1500, // 25 minutes in seconds
      timer: null
    };
  },
  computed: {
    formatTime() {
      const minutes = Math.floor(this.timeLeft / 60);
      const seconds = this.timeLeft % 60;
      return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
  },
  methods: {
    startTimer() {
      this.timerRunning = true;
      this.timer = setInterval(() => {
        if (this.timeLeft > 0) {
          this.timeLeft--;
        } else {
          this.stopTimer();
          // Timer finished, do something here
        }
      }, 1000);
    },
    stopTimer() {
      this.timerRunning = false;
      clearInterval(this.timer);
    }
  }
};
</script>

<style scoped>
.timer {
  text-align: center;
}
h1 {
  font-size: 48px;
  margin-bottom: 20px;
}
button {
  font-size: 24px;
  padding: 10px 20px;
}
</style>

