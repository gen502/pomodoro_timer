<template>
    <div class="StretchTime">

      <!-- ゲージの表示 -->
      <div class="progress-bar">
          <div class="progress" :style="{ width: progressRatio + '%' }"></div>
      </div>

      <!-- タイマーの表示 -->
      <div class="formatTime">{{ formatTime(remainingTime) }}</div>
      
      <div class="avatars">
            <div class="myavatar"><iframe src="http://localhost:1234" width="100%" height="100%" frameborder=0></iframe></div>
            <!-- 動画をオーバーレイで載せる -->
            
              <video width="500" height="800" src="/shoulder.mov" autoplay muted playsinline style="margin-left: -4%;" id="trainervideo"></video>
            
            
      </div>  

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
        <button class="minimize-button" @click="toggleMinimize" style="color: white;">
                <WatermarkIcon :size="18" style="margin-right: 1px; margin-top: 2px;"/>
        </button>

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
// import videojs from 'video.js';
// import 'video.js/dist/video-js.css'; // video.jsのCSSファイルをインポート

var webSocket; //ウェブソケット

// サーバにメッセージを送信する関数
function sendMessage(message){
  console.dir(message);
  webSocket.send(JSON.stringify(message));
}

var msg = {
        'option' : 'stretch',
    }


export default {
  data() {
    return {
      selected: null,
      remainingTime: 5 * 60, // 初期値として5分を秒単位で設定
      progressRatio: 100, // ゲージの初期値を100%として設定
      timerRunning: true, // タイマーが実行中かどうかのフラグ
      showComponent: true, // v-ifディレクティブの条件に基づいてコンポーネントを再生成するフラグ
    };
  },
  computed: {
        ...mapState(['workTime', 'breakTime', 'setCount']),
    },
  mounted() {
    // this.initVideoPlayer();
    webSocket = new WebSocket("ws://localhost:8001"); // インスタンスを作り、サーバと接続
    // ソケット接続すれば呼び出す関数を設定
    webSocket.onopen = function(message){
        //messageTextArea.value += "Server connect... OK\n";
        console.log(message);
        sendMessage(msg);
        
    };

    // ソケット接続が切ると呼び出す関数を設定
    webSocket.onclose = function(message){
        //messageTextArea.value += "Server Disconnect... OK\n";
        console.log(message);
    };

    // ソケット通信中でエラーが発生すれば呼び出す関数を設定
    webSocket.onerror = function(message){
        console.log(message);
        //messageTextArea.value += "error...\n";
    };

    // ソケットサーバからメッセージが受信すれば呼び出す関数を設定
    webSocket.onmessage = function(message){
        console.log(message.data);
        const imgElement = document.getElementById('trainervideo');
        imgElement.src = message.data;
        webSocket.close();
        //messageTextArea.value += "Receive => "+message.data+"\n";
    };
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
          this.remainingTime = this.breakTime * 10;
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
    // initVideoPlayer() {
    //     const options = {
    //         autoplay: true,
    //     };
    //     this.player = videojs('my-video', options, function onPlayerReady() {
    //     // プレーヤーが初期化された時に実行する処理（必要に応じて）
    //   });
    // },      
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
    width: 45%;
    height: auto;
    /* border-radius: 50%; */
    /* background: #ffffff; */
    /* margin-top: 170px; */
    margin-left: 10%;
    transform: scale(-1, 1);  /*左右反転*/
    /* overflow: hidden; */
    /* margin-right: auto; */
    /* box-shadow: 0px 0px 20px 2px #4FA095 */
}

video{
  clip-path:circle(40% at 50% 50%);
}

.trainer{
  width: 50%;
  margin-left: -25%;
  /* height: 50%; */
  /* border-radius: 50%;
  overflow: hidden; */
}

.settingbutton{
  position: fixed;
  right: 20px;
  bottom: 20px;
  display: flex;
  justify-content: flex-end;
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

.minimize-button {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #92A09E;
    border: none;
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

.avatars{
    display: flex;
    filter: drop-shadow(0px 0px rgba(0,0,0,0));
}

</style>