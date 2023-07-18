<template>
    <form @submit.prevent="saveSettings">
        <div class="settings">
            <div class="container">
                <div class="settingtitle">
                    <CogIcon style="margin-top: 10px; margin-left: 15px; margin-right: 5px;"/>    
                    <h1>設定</h1>
                </div>    
                <hr>
                <form>
                    <div style="margin-right: 375px;">タイマー設定</div>
                    <label for="work-time">作業時間:</label>
                    <select id="work-time" name="work-time" required>
                        <option value="" disabled selected>作業時間を選択</option>
                        <option value="work_15min">15分</option>
                        <option value="work_25min">25分</option>
                        <option value="work_35min">35分</option>
                        <option value="work_45min">45分</option>
                        <option value="work_55min">55分</option>
                        <option value="work_60min">60分</option>
                    </select><br>

                    <label for="break-time">休憩時間:</label>
                    <select id="break-time" name="break-time" required>
                        <option value="" disabled selected>休憩時間を選択</option>
                        <option value="break_5min">5分</option>
                        <option value="break_10min">10分</option>
                        <option value="break_15min">15分</option>
                        <option value="break_25min">25分</option>
                        <option value="break_30min">30分</option>
                    </select><br>

                    <label for="set-count">セット数:</label>
                    <select id="set-count" name="set-count" required>
                        <option value="" disabled selected>セット数を選択</option>
                        <option value="set_1">1</option>
                        <option value="set_2">2</option>
                        <option value="set_3">3</option>
                        <option value="set_4">4</option>
                        <option value="set_5">5</option>
                        <option value="set_6">6</option>
                        <option value="set_7">7</option>
                        <option value="set_8">8</option>
                        <option value="set_9">9</option>
                        <option value="set_10">10</option>
                    </select><br>

                    <div style="margin-right: 400px;">体の悩み</div>
                    <div class="options">
                        <p class="option" id="首こり">首こり</p>
                        <p class="option" id="肩こり">肩こり</p>
                        <p class="option" id="背中痛">背中痛</p>
                        <p class="option" id="猫背">猫背</p>
                        <p class="option" id="手首">手首</p>
                    </div><br>

                    <div class="save-button">
                        <input type="submit" value="Save">
                    </div>
                </form>
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
        ...mapMutations(['setWorkTime', 'setBreakTime', 'setSetCount']),
        saveSettings() {
            const workTimeSelect = document.getElementById('work-time');
            const breakTimeSelect = document.getElementById('break-time');
            const setCountSelect = document.getElementById('set-count');
            const workTime = workTimeSelect.options[workTimeSelect.selectedIndex].value;
            const breakTime = breakTimeSelect.options[breakTimeSelect.selectedIndex].value;
            const setCount = setCountSelect.options[setCountSelect.selectedIndex].value;
            this.setWorkTime(workTime);
            this.setBreakTime(breakTime);
            this.setSetCount(setCount);
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
}

.settingtitle{
    display: flex;
    align-items: center;
    margin-bottom: -10px;
}
.container {
    max-width: 500px;
    margin: auto;
    margin-top: 95px;
    text-align: center;
    background-color: #ffffff;
    border-radius: 3%;
}

h1 {
    font-size: 24px;
    margin-top: 20px;
}

label {
    font-size: 20px;
    margin-right: 10px;
}

select {
    font-size: 20px;
    padding: 5px 10px;
    border: none;
    border-radius: 5px;
    background-color: #eee;
    margin-bottom: 10px;
}

.options {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    margin-top: 30px;
    width: 60%;
    margin-left: 20%;
}

.option {
    padding: 20px;
    font-size: 15px;
    font-weight: bold;
    text-align: center;
    background-color: #fff;
    border: 3px solid #333;
    border-radius: 10px;
    cursor: pointer;
}

.option.selected {
    background-color: green;
    color: #fff;
}

.option:hover {
    background-color: #333;
    color: #fff;
}

.save-button {
  margin-top: 30px;
}

.save-button input[type="submit"] {
  padding: 15px 30px;
  font-size: 20px;
  font-weight: bold;
  background-color: #333;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.save-button input[type="submit"]:hover {
  background-color: #555;
}

</style>
