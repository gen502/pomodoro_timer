<!--<template>
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
</style>-->

<!-- template>
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
      timer: null,
      fullCircle: 565, // Circumference of full circle (2 * π * radius)
      gaugeOffset: 0 // Initial gauge offset
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
          this.gaugeOffset = ((this.fullCircle * (1500 - this.timeLeft)) / 1500).toFixed(2);
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
</style>-->

<template>
  <SettingVue msg="Hello World!" />
</template>

<script>
import SettingVue from './components/setting.vue'

export default {
  name: 'App',
  components: {
    SettingVue
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