<template>
    <div class="StretchTime">

        <!-- ゲージの表示 -->
        <div class="progress-bar">
            <div class="progress" :style="{ width: progressRatio + '%' }"></div>
        </div>

        <!-- タイマーの表示 -->
        <div class="formatTime">{{ formatTime(remainingTime) }}</div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      remainingTime: 5 * 60, // 初期値として5分を秒単位で設定
      progressRatio: 100, // ゲージの初期値を100%として設定
    };
  },
  mounted() {
    setInterval(this.updateRemainingTime, 1000); // 1秒ごとに残り時間を更新
  },
  methods: {
    updateRemainingTime() {
      if (this.remainingTime > 0) {
        this.remainingTime--; // 残り時間を1秒減らす
        this.progressRatio = (this.remainingTime / (5 * 60)) * 100; // 残り時間の割合を計算
      }
    },
    formatTime(time) {
      const minutes = Math.floor(time / 60); // 分単位の時間を計算
      const seconds = time % 60; // 秒単位の時間を計算
      return `${minutes}:${seconds.toString().padStart(2, '0')}`; // MM:SS 形式で表示する
    },
  },
};

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

</style>
