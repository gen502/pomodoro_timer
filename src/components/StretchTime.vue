<template>
  <div class="StretchTime">

    <div class="progress-bar">
      <div class="progress" :style="{ width: progressRatio + '%' }"></div>
    </div>

    <div class="formatTime">{{ formatTime(remainingTime) }}</div>
    <div class="content">
      <div v-if="!buttonClicked">
        <div class="video-container">
          <div class="myavatar"></div>
          <video ref="video" width="500" height="300" :src="sampleURL" autoplay muted @ended="stopRecording" playsinline style="margin-left: 50px; margin-top: 80px;"></video>
        </div>
      </div>
      <div v-else-if="buttonClicked">
        <div v-if="isLoading">
          Processing...
        </div>
        <div v-else>
          <div class = "video-container">
            <video ref="video1" width="500" height="300" :src="actURL_a" autoplay muted playsinline style="margin-left: 50px; margin-top: 80px;"></video>
            <video ref="video2" width="500" height="300" :src="sampleURL_s" autoplay muted playsinline style="margin-left: 50px; margin-top: 80px;"></video>
            <img v-if="showImage" class="overlay-image" src="/img/test.jpeg" alt="Some image" />
          </div>
        </div>
      </div>
    </div>


    <div class="settingbutton">
      <div class="stop" @click="toggleTimer" style="color: white;">
        <component :is="timerRunning ? 'PauseIcon' : 'PlayIcon'" style="margin-right: 1px; margin-top: 3px;"/>
      </div>
      <div class="setting" style="color: white;">
        <CogIcon :size="23" style="margin-right: 2px; margin-top: 5px;" />
      </div>
      <div class="minimaize" style="color: white; ">
        <WatermarkIcon :size="17" style="margin-right: 1px; margin-top: 3px;"/>
      </div>

    </div>

    <div>
      <button @click="process">フィードバックを生成する！</button>
    </div>
    <div>
      <button @click="showImage = !showImage">もっと詳しく</button>
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
import axios from 'axios';

export default {
  data() {
    return {
      remainingTime: 5 * 60, // 初期値として5分を秒単位で設定
      progressRatio: 100, // ゲージの初期値を100%として設定
      timerRunning: true, // タイマーが実行中かどうかのフラグ
      buttonClicked: false,
      isLoading: false,
      imageURL: '/sampleoutput/frame_0.jpg',
      processResult: null,
      sampleURL: '/samplevideo/1/test1.mp4',
      // sampleURL: '/test1.mp4',
      sampleURL_s: '/test1.mp4',
      // actURL_a :'/actoutput_video/video1.mp4',
      actURL_a: '/test1.mp4',
      showImage: false,
    };
  },
  computed: {
    ...mapState(['workTime', 'breakTime', 'setCount']),
  },
  mounted() {
    this.remainingTime = this.breakTime * 10;
    this.startTimer();
    this.startRecording();
    this.startPlaying();
  },
  components: {
    PauseIcon,
    PlayIcon,
    ResetIcon,
    WatermarkIcon,
    CogIcon,

  },
  methods: {
    async startRecording() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
        this.mediaRecorder = new MediaRecorder(stream);
        this.chunks = [];

        this.mediaRecorder.ondataavailable = event => {
          this.chunks.push(event.data);
        };
        this.mediaRecorder.onstop = () => {
          const blob = new Blob(this.chunks, { type: 'video/mp4' });
          const url = URL.createObjectURL(blob);
          const link = document.createElement('a');
          link.href = url;
          link.download = 'recorded-video.mp4';
          link.click();
        };

        this.mediaRecorder.start();
      } catch (error) {
        console.error(error);
      }
    },
    stopRecording() {
      if (this.mediaRecorder && this.mediaRecorder.state !== 'inactive') {
        this.mediaRecorder.stop();
      }
    },

    ...mapMutations(['decreaseSetCount']),
    async startPlaying(videoUrl, refName, shouldStopRecording = false) {
      if (this.$refs[refName]) {
        const response = await fetch(videoUrl);
        const blob = await response.blob();
        this.$refs[refName].src = URL.createObjectURL(blob);
        this.$refs[refName].oncanplay = () => {
          if (shouldStopRecording) {
            this.$refs[refName].onended = this.stopRecording;
          }
          this.$refs[refName].play();
          console.log(refName)
        }
      }
    },

    async process() {
      this.buttonClicked = true;
      this.isLoading = true;
      try {
        const response = await axios.post('http://127.0.0.1:5000/api/process');
        this.processResult = response.data;
        this.isLoading = false;
        await this.startPlaying(this.sampleURL, 'video', true);  //第一个视频结束后，停止录制
        await this.startPlaying(this.actURL_a, 'video1');  //在录制内容可用时开始播放
        await this.startPlaying(this.sampleURL_s, 'video2');  //在录制内容可用时开始播放
      } catch (error) {
        console.error(error);
        this.isLoading = false;
      }
    },

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
    // resetTimer() {
    //   this.stopTimer();
    //   this.remainingTime = this.breakTime * 60;
    //   this.progressRatio = 100;
    //   this.timerRunning = true;
    //   this.startTimer();
    // },
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
  beforeUnmount() {
    this.stopRecording();
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


.content {
  display: flex;
  flex-direction: row;
}

@media (max-width: 600px) {
  .content {
    flex-direction: column;
  }
}

.video-container {
  display: flex;
  align-items: center; /* if you want to align items vertically center */
  position: relative;
}

.overlay-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 10;
}




</style>




