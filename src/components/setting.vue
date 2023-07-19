<template>
    <form @submit.prevent="saveSettings">
        <div class="settings">
            <div class="container">
                <div class="settingtitle">
                    <CogIcon style="margin-top: 10px; margin-left: 15px; margin-right: 5px; color: #5B5B5B;"/>    
                    <h1>設定</h1>
                </div>    
                <hr>
                <div class="settingContents">
                    <div class="subtitle" style="margin-top: 10px; color: #5B5B5B;">タイマー設定</div>
                    <!-- 作業時間の設定 -->
                    <div class="settingwork" style="margin-top: 5px;">
                        <label for="work-time" style="font-size: 16px;">作業時間:</label>
                        <select id="work-time" name="work-time" style="font-size: 16px; cursor: pointer;" required >
                            <option value="" disabled selected>作業時間を選択</option>
                            <option value="1">1分</option>
                            <option value="25">25分</option>
                            <option value="35">35分</option>
                            <option value="45">45分</option>
                            <option value="55">55分</option>
                            <option value="60">60分</option>
                        </select>
                    </div>

                    <!-- 休憩時間の設定 -->
                    <div class="settingbreak">
                        <label for="break-time" style="font-size: 16px;">休憩時間:</label>
                        <select id="break-time" name="break-time"  style="font-size: 16px; cursor: pointer;" required>
                            <option value="" disabled selected>休憩時間を選択</option>
                            <option value="1">1分</option>
                            <option value="10">10分</option>
                            <option value="15">15分</option>
                            <option value="25">25分</option>
                            <option value="30">30分</option>
                        </select>
                    </div>

                    <!-- セット数の設定 -->
                    <div class="settingset">
                        <label for="set-count" style="font-size: 16px;">セット数:</label>
                        <select id="set-count" name="set-count" style="font-size: 16px; cursor: pointer;" required>
                            <option value="" disabled selected>セット数を選択</option>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                            <option value="6">6</option>
                            <option value="7">7</option>
                            <option value="8">8</option>
                            <option value="9">9</option>
                            <option value="10">10</option>
                        </select><br>
                    </div>

                    <div class="subtitle" style="color: #5B5B5B;">体の悩み</div>
                    <div class="options">
                        <div class="optionsnarabi" style="margin-top: -15px;">
                            <p class="option" :class="{ selected: selected === '首こり' }" id="首こり" @click="selectOption('首こり')">首こり</p>
                            <p class="option" :class="{ selected: selected === '肩こり' }" id="肩こり" @click="selectOption('肩こり')">肩こり</p>
                            <p class="option" :class="{ selected: selected === '背中痛' }" id="背中痛" @click="selectOption('背中痛')">背中痛</p>
                        </div>
                        <div class="optionsnarabi2">    
                            <p class="option" :class="{ selected: selected === '猫背' }" id="猫背" @click="selectOption('猫背')">猫背</p>
                            <p class="option" :class="{ selected: selected === '手首' }" id="手首" @click="selectOption('手首')">手首</p>
                        </div>    
                        </div><br>
                </div>    

                <div class="save-button">
                    <input type="submit" value="Save">
                </div>
            </div>
        </div>
    </form>    
</template>

<script>
import CogIcon from "vue-material-design-icons/Cog.vue";
import { mapMutations } from 'vuex';

export default {
    name: 'SettingVue',
    methods: {
        selectOption(id) {
            this.selected = id;
        },
        ...mapMutations(['setWorkTime', 'setBreakTime', 'setSetCount']),
        saveSettings() {
            const workTimeSelect = document.getElementById('work-time');
            const breakTimeSelect = document.getElementById('break-time');
            const setCountSelect = document.getElementById('set-count');
            const workTime = parseInt(workTimeSelect.options[workTimeSelect.selectedIndex].value);
            const breakTime = parseInt(breakTimeSelect.options[breakTimeSelect.selectedIndex].value);
            const setCount = parseInt(setCountSelect.options[setCountSelect.selectedIndex].value);
            this.setWorkTime(workTime);
            this.setBreakTime(breakTime);
            this.setSetCount(setCount);
            this.$router.push('/firsttimer');
        }
    },
    components: {
        CogIcon,
    },
}
</script>

<style scoped>

.settings {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: #fffbec;
    display: flex;
    align-items: center;
}

.settingtitle{
    display: flex;
    align-items: center;
    margin-bottom: -10px;
}
.container {
    width: 480px;
    margin: 0 auto;
    /* margin-top: 100px; */
    text-align: center;
    background-color: #ffffff;
    border-radius: 5%;
    box-shadow:0px 0px 5px rgba(0, 0, 0, 0.12);
    
}

h1 {
    font-size: 24px;
    margin-top: 20px;
    color: #5B5B5B;
}

label {
    font-size: 20px;
    margin-right: 10px;
}

select {
    font-size: 20px;
    padding: 5px 15px;
    border: none;
    outline: none;
    border-radius: 15px;
    background-color: #eee;
    margin-bottom: 10px;
}

.options {
    display: flex;
    flex-flow: column;
    margin: auto;
    /* justify-content: space-around;
    flex-wrap: wrap;
    margin-top: 30px;
    width: 60%;
    margin-left: 20%; */
}

.option {
    padding-left: 15px;
    padding-right: 15px;
    padding-top: 4px;
    padding-bottom: 4px;
    margin: 5px;
    margin-top: 20px;
    font-size: 14px;
    /* font-weight: bold; */
    text-align: center;
    background-color: #EFF2F0;
    /* border: 2px solid #333; */
    border-radius: 20px;
    cursor: pointer;
}

.option.selected {
    background-color: green;
    color: #fff;
}

.option:hover {
    background-color: #999;
    color: #fff;
}

.optionsnarabi{
    display: flex;
}
.optionsnarabi2{
    display: flex;
    margin: auto;
    margin-top: -10px;
}

.save-button {
  margin-top: 30px;
}

.save-button input[type="submit"] {
  padding: 10px 18px;
  font-size: 20px;
  font-weight: bold;
  background-color: #4FA095;
  color: #fff;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  margin-bottom: 30px;
}

.save-button input[type="submit"]:hover {
  background-color: #528C84;
  box-shadow:0px 0px 20px rgba(0, 0, 0, 0.1);
}

.settingContents{
  display:flex;
  flex-flow: column;
}

.settingwork,
.settingbreak,
.settingset {
    display:flex;
    margin:0 auto;
}

.subtitle {
    margin-right: auto;
    margin-left: 18px;
    font-weight: bold;
    font-size: 17px;
}
</style>
