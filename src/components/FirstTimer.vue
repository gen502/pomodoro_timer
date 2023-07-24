<head>
</head>

<template>
    <div class="Time" :class="{ 'minimized': isMinimized }">
        <!-- ゲージと時間の表示 -->
        <div class="circle-progress" v-if="!isMinimized">
            <svg xmlns="http://www.w3.org/2000/svg" class="progress-ring" :width="circleSize" :height="circleSize">
                <circle class="progress-ring-circle" :stroke="progressColor" stroke-width="20" fill="transparent"
                    :r="circleRadius" :cx="circleCenter" :cy="circleCenter"
                    :style="{ strokeDasharray: getCircumference(), strokeDashoffset: progressOffset }"></circle>
                <g :transform="`translate(${circleCenter}, ${circleCenter})`">
                    <text class="progress-text" dominant-baseline="middle" text-anchor="middle"
                        :style="{ fill: progressColor }">
                        {{ formatTime(remainingTime) }}
                    </text>
                </g>
            </svg>

            <div class="button-container">
                <button class="play-pause-button" @click="toggleTimer" style="color: white;" :disabled="isMinimized && !isCursorOverMinimizeButton">
                    <component :is="timerRunning ? 'PauseIcon' : 'PlayIcon'" />
                </button>
                <button class="reset-button" @click="resetTimer" style="color: white;" :disabled="isMinimized && !isCursorOverMinimizeButton">
                    <ResetIcon :size="25" />
                </button>
            </div>
        </div>
        <div class="minimized-timer" v-else>
            <svg xmlns="http://www.w3.org/2000/svg" class="progress-ring" :width="circleSize" :height="circleSize">
                <circle class="progress-ring-circle" :stroke="progressColor" stroke-width="20" fill="transparent"
                    :r="circleRadius" :cx="circleCenter" :cy="circleCenter"
                    :style="{ strokeDasharray: getCircumference(), strokeDashoffset: progressOffset }"></circle>
                <g :transform="`translate(${circleCenter}, ${circleCenter})`">
                    <text class="progress-text" dominant-baseline="middle" text-anchor="middle"
                        :style="{ fill: progressColor }">
                        {{ formatTime(remainingTime) }}
                    </text>
                </g>
            </svg>

            <div class="button-container">
                <button class="play-pause-button" @click="toggleTimer" style="color: white;">
                    <component :is="timerRunning ? 'PauseIcon' : 'PlayIcon'" />
                </button>
                <button class="reset-button" @click="resetTimer" style="color: white;">
                    <ResetIcon :size="25" />
                </button>
            </div>
        </div>

        <div class="settingcontainer">
            <div class="setting" style="color: white;" @click="navigateToSettings">
                <CogIcon :size="23" style="margin-right: 2px; margin-top: 5px;" />
            </div>
            <!-- 最小化ボタン -->
            <button class="minimize-button" @click="toggleMinimize" style="color: white;">
                <WatermarkIcon :size="18" style="margin-right: 1px; margin-top: 2px;"/>
            </button>
        </div>
    </div>
</template>


<script>
import PauseIcon from "vue-material-design-icons/Pause.vue";
import PlayIcon from "vue-material-design-icons/Play.vue";
import ResetIcon from "vue-material-design-icons/Restore.vue";
import WatermarkIcon from "vue-material-design-icons/Watermark.vue";
import CogIcon from "vue-material-design-icons/Cog.vue";
import { mapState } from 'vuex';
const { remote } = require('electron')
const win = remote.getCurrentWindow()
// import { useRouter } from 'vue-router'

export default {
    data() {
        return {
            remainingTime: 5 * 60, // 初期値として5分を秒単位で設定
            progressRatio: 100, // ゲージの初期値を100%として設定
            circleSize: 300, // ゲージのサイズ
            circleRadius: 140, // ゲージの半径
            circleCenter: 150, // ゲージの中心座標
            progressColor: "#4FA095", // ゲージの色
            timerRunning: true, // タイマーが実行中かどうかのフラグ
            isMinimized: false, // 最小化されているかどうかのフラグ
            isCursorOverMinimizeButton: false,
        };
    },
    computed: {
        ...mapState(['workTime', 'breakTime', 'setCount']),
        progressOffset() {
            return (1 - this.progressRatio / 100) * this.getCircumference();
        },
    },
    components: {
        PauseIcon,
        PlayIcon,
        ResetIcon,
        WatermarkIcon,
        CogIcon
    },
    mounted() {
        this.remainingTime = this.workTime * 10;
        this.startTimer();
    },
    methods: {
        async toggleMinimize() {
            const { ipcRenderer } = require('electron');
            if (this.isMinimized) {
                await ipcRenderer.invoke('set-ignore-mouse-events', false);
                this.isMinimized = false;
            } else {
                await ipcRenderer.invoke('set-ignore-mouse-events', true);
                this.isMinimized = true;
            }
        },
        onMouseEnter() {
            this.isCursorOverMinimizeButton = true;
            win.setIgnoreMouseEvents(false)
        },
        onMouseLeave() {
            this.isCursorOverMinimizeButton = false;
            win.setIgnoreMouseEvents(true, { forward: true })
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
        resetTimer() {
            this.stopTimer();
            this.remainingTime = this.workTime * 10;
            this.progressRatio = 100;
            this.timerRunning = true;
            this.startTimer();
        },
        updateRemainingTime() {
            if (this.remainingTime > 0) {
                this.remainingTime--; // 残り時間を1秒減らす
                this.progressRatio = (this.remainingTime / (this.workTime * 10)) * 100; // 残り時間の割合を計算
            } else {
                this.stopTimer();
                this.$router.push('/stretch');
            }
        },
        formatTime(time) {
            const minutes = Math.floor(time / 60); // 分単位の時間を計算
            const seconds = time % 60; // 秒単位の時間を計算
            return `${minutes}:${seconds.toString().padStart(2, "0")}`; // MM:SS 形式で表示する
        },
        getCircumference() {
            const radius = this.circleRadius;
            return 2 * Math.PI * radius;
        },
        navigateToSettings() {
            this.$router.push('/setting');
        },
    },
};
</script>

<style scoped>
.Time {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: #FFFBEC;
    background-repeat: no-repeat;
    background-size: cover;
}

.circle-progress {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.progress-ring-circle {
    transition: stroke-dashoffset 0.35s;
    transform: rotate(90deg) scaleX(-1);
    transform-origin: 50% 50%;
}

.progress-text {
    margin-bottom: 10px;
    font-size: 60px;
    font-weight: bold;
}

.button-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}

.play-pause-button,
.reset-button {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background-color: #4FA095;
    border: none;
    margin: 0 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}

.play-pause-button:hover,
.reset-button:hover {
    background-color: #58bfa7;
}

.settingcontainer {
    display: flex;
    position: fixed;
    right: 20px;
    bottom: 20px;
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

.minimize-button:hover {
    background-color: #b0b9b5;
}

.minimized-timer {
    position: fixed;
    border-radius: 12px;
    padding: 5px 10px;
    font-size: 50px;
    font-weight: bold;
    width: 100vw;
    /* 幅を追加 */
    height: 100vh;
    /* 高さを追加 */
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}


.setting {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #92A09E;
    margin: 7px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}
</style>