<template>
    <div class="FeedBack">
      <div class="comment1">今回のストレッチはどうでしたか？</div>
      <div v-for="index in setCount" :key="index" class="StretchFB">
        <div class="Stretch"></div>
        <div class="FB">
          <div class="icon-wrapper">
            <ThumbUpOutline
              :size="24"
              :class="{ active: feedbackValues[index] === 'thumbUp' }"
              @click="handleThumbClick(index, 'thumbUp')"
            />
          </div>
          <div class="icon-spacing"></div>
          <div class="icon-wrapper">
            <ThumbDownOutline
              :size="24"
              :class="{ active: feedbackValues[index] === 'thumbDown' }"
              @click="handleThumbClick(index, 'thumbDown')"
            />
          </div>
        </div>
      </div>
      <div class="comment2">フィードバックありがとうございます！お疲れ様でした！</div>
      <div class="backbutton">
        <div class="backtext">戻る</div>
      </div>
    </div>
  </template>
  
  <script>
  import ThumbUpOutline from "vue-material-design-icons/ThumbUpOutline.vue";
  import ThumbDownOutline from "vue-material-design-icons/ThumbDownOutline.vue";
  
  export default {
    components: {
      ThumbUpOutline,
      ThumbDownOutline,
    },
    data() {
      return {
        setCount: 5, // 表示するセット数を指定
        feedbackValues: {}, // アイコンの状態を保持するためのオブジェクト
      };
    },
    methods: {
      handleThumbClick(index, type) {
        if (type === "thumbUp") {
          this.feedbackValues[index] = "thumbUp"; // ThumbUpアイコンが選択された場合の状態を設定
          delete this.feedbackValues[index + "thumbDown"]; // ThumbDownアイコンの状態をリセット
        } else if (type === "thumbDown") {
          this.feedbackValues[index] = "thumbDown"; // ThumbDownアイコンが選択された場合の状態を設定
          delete this.feedbackValues[index + "thumbUp"]; // ThumbUpアイコンの状態をリセット
        }
        if (this.feedbackValues[index] === "thumbUp") {
          console.log(1);
        } else if (this.feedbackValues[index] === "thumbDown") {
          console.log(-1);
        } else {
          console.log(0);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .FeedBack {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: #fffbec;
    background-image: url("./pattern-image.png");
    background-repeat: no-repeat;
    background-size: cover;
    text-align: center;
  }
  
  .comment1 {
    text-align: center;
    margin-top: 110px;
    margin-bottom: 80px;
    color: #382823;
    font-weight: bold;
    font-size: 20px;
  }
  
  .Stretch {
    text-align: center;
    width: 160px;
    height: 160px;
    border-radius: 50%;
    background: #e5f3e7;
    margin-left: 6px;
    margin-right: 6px;
  }
  
  .StretchFB {
    display: inline-block;
  }
  
  .FB {
    display: flex;
    justify-content: center;
  }
  
  .icon-wrapper {
    margin: 10px;
    /* 余白の幅を調整してください */
    cursor: pointer;
    color: #737373;
  }
  
  .comment2 {
    position: fixed;
    bottom: 100px;
    /* 画面下からの距離を指定 */
    left: 50%;
    transform: translateX(-50%);
    /* 水平方向に中央揃え */
    color: #382823;
    font-weight: bold;
    font-size: 20px;
  }
  
  .backbutton {
    position: fixed;
    bottom: 45px;
    /* 画面下からの距離を指定 */
    left: 50%;
    transform: translateX(-50%);
    /* 水平方向に中央揃え */
    width: 120px;
    height: 40px;
    border-radius: 20px;
    background: #4fa095;
    margin-top: 40px;
    margin-left: auto;
    margin-right: auto;
    cursor: pointer;
    box-shadow: 0 0 5px #737373;
  }
  
  .backtext {
    font-weight: bold;
    text-align: center;
    padding-top: 7px;
    color: #fffbec;
  }
  
  .active {
    color: #42887e;
    /* アクティブな状態の色を指定 */
  }
  </style>