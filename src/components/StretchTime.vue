<template>
    <div class="StretchTime">

      <!-- ゲージの表示 -->
      <div class="progress-bar">
          <div class="progress" :style="{ width: progressRatio + '%' }"></div>
      </div>

      <!-- タイマーの表示 -->
      <div class="formatTime">{{ formatTime(remainingTime) }}</div>
    
      <div class="myavatar"></div>

      <div class="settingbutton">
        <div class="stop" @click="toggleTimer" style="color: white;">
          <component :is="timerRunning ? 'PauseIcon' : 'PlayIcon'" style="margin-right: 1px; margin-top: 3px;"/>
        </div>
        <div class="restart" @click="resetTimer" style="color: white;">
          <ResetIcon :size="24" style="margin-right: 3px; margin-top: 3px;" />
        </div>
        <div class="setting" style="color: white;">
          <CogIcon :size="23" style="margin-right: 2px; margin-top: 5px;" />
        </div>
        <div class="minimaize" style="color: white; ">
          <WatermarkIcon :size="17" style="margin-right: 1px; margin-top: 3px;"/>
        </div>

      </div>
    
    </div>
</template>

<script>
// import { mapMutations } from 'vuex';
import PauseIcon from "vue-material-design-icons/Pause.vue";
import PlayIcon from "vue-material-design-icons/Play.vue";
import ResetIcon from "vue-material-design-icons/Restore.vue";
import WatermarkIcon from "vue-material-design-icons/Watermark.vue";
import CogIcon from "vue-material-design-icons/Cog.vue";
import { mapState, mapMutations } from 'vuex';

export default {
  data() {
    return {
      remainingTime: 5 * 60, // 初期値として5分を秒単位で設定
      progressRatio: 100, // ゲージの初期値を100%として設定
      timerRunning: true, // タイマーが実行中かどうかのフラグ
    };
  },
  computed: {
        ...mapState(['workTime', 'breakTime', 'setCount']),
    },
  mounted() {
    this.remainingTime = this.breakTime * 10;
    this.startTimer();
  },
  components: {
        PauseIcon,
        PlayIcon,
        ResetIcon,
        WatermarkIcon,
        CogIcon,
    },
  methods: {
    ...mapMutations(['decreaseSetCount']),
    startTimer() {
        this.timer = setInterval(this.updateRemainingTime, 1000); // 1秒ごとに残り時間を更新
      },
    stopTimer() {
         clearInterval(this.timer);
      },
    toggleTimer() {
          if (this.timerRunning) {
              this.stopTimer();
          } else {
              this.startTimer();
          }
          this.timerRunning = !this.timerRunning;
      },
    resetTimer() {
          this.stopTimer();
          this.remainingTime = this.breakTime * 60;
          this.progressRatio = 100;
          this.timerRunning = true;
          this.startTimer();
      },
    updateRemainingTime() {
      if (this.remainingTime > 0) {
        this.remainingTime--; // 残り時間を1秒減らす
        this.progressRatio = (this.remainingTime / (this.breakTime * 10)) * 100; // 残り時間の割合を計算
      } else {
        this.stopTimer();
        if (this.setCount > 1) {
            // セットカウントを1減らす
            this.decreaseSetCount();
            this.$router.push('/firsttimer'); 
        } else {
            this.$router.push('/feedback');
        }
      }
    },
    formatTime(time) {
      const minutes = Math.floor(time / 60); // 分単位の時間を計算
      const seconds = time % 60; // 秒単位の時間を計算
      return `${minutes}:${seconds.toString().padStart(2, '0')}`; // MM:SS 形式で表示する
    },
  },
};

// import PauseIcon from "vue-material-design-icons/Pause.vue";

</script>


<style scoped>
.StretchTime{
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: radial-gradient(45.97% 45.97% at 50% 50%, #FFFBEC 23.12%, rgba(255, 255, 255, 0) 100%), #E5F3E7;
  background-image: url("./pattern-image.png");
  background-repeat: no-repeat;
  background-size: cover;
}

.progress-bar {
  /* width: 90vw; */
  height: 23px;
  background-color: #D9D9D9;
  border-radius: 20px; /* ゲージに丸みをつける */
  margin-top: 50px;
  margin-right: 275px;
  margin-left: 275px;
}

.progress {
  height: 100%;
  background-color:#4FA095;
  border-radius: 20px; /* ゲージに丸みをつける */
}

.formatTime{
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #4FA095;
}

.myavatar{
    /* text-align: center; */
    width: 250px;
    height: 250px;
    border-radius: 50%;
    background: #ffffff;
    margin-top: 170px;
    margin-left: 300px;
    /* margin-right: auto; */
    /* box-shadow: 0px 0px 20px 2px #4FA095 */
}

.settingbutton{
  display: flex;
  justify-content: flex-end;
  margin-top: 140px;
  margin-right: 15px;
}

.stop{
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background:#4FA095;
  margin: 7px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;

}

.restart{
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background:#4FA095;
  margin: 7px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;

}

.setting{
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background:#92A09E;
  margin: 7px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.minimaize{
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background:#92A09E;
  margin: 7px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.stop:hover,
.restart:hover{
    background-color: #58bfa7;
}

.setting:hover,
.minimaize:hover{
  background-color: #ADB9B7;
}

</style>