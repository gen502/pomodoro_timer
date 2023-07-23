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
                            <p class="option" :class="{ selected: concerns.首こり }" @click="toggleConcern('首こり')">首こり</p>
                            <p class="option" :class="{ selected: concerns.肩こり }" @click="toggleConcern('肩こり')">肩こり</p>
                            <p class="option" :class="{ selected: concerns.背中痛 }" @click="toggleConcern('背中痛')">背中痛</p>
                        </div>
                        <div class="optionsnarabi2">    
                            <p class="option" :class="{ selected: concerns.猫背 }" @click="toggleConcern('猫背')">猫背</p>
                            <p class="option" :class="{ selected: concerns.手首 }" @click="toggleConcern('手首')">手首</p>
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
import axios from 'axios';

var webSocket; //ウェブソケット


    // サーバにメッセージを送信する関数
    function sendMessage(message){
      //var message = document.getElementById("textMessage");
      //console.log(message.value);
      //var message = {"id": 12, "name":"gen"};
      //messageTextArea.value += "Send => "+message.value+"\n";
      //webSocket.send(message.value);
      console.dir(message);
      webSocket.send(JSON.stringify(message));
      //message.value = "";
    }

   

export default {
    name: 'SettingVue',
    data() {
        return {
            concerns: {
                '首こり': false,
                '肩こり': false,
                '背中痛': false,
                '猫背': false,
                '手首': false
            }
        };
    },
    methods: {
        selectOption(id) {
            this.selected = id;
        },
        toggleConcern(id) {
            this.concerns[id] = !this.concerns[id];
            console.log(this.concerns);
        },
        ...mapMutations(['setWorkTime', 'setBreakTime', 'setSetCount']),
        async saveSettings() {
            const concernsArray = Object.keys(this.concerns).map(key => this.concerns[key] ? 1 : 0);
            console.log(concernsArray);
            const workTimeSelect = document.getElementById('work-time');
            const breakTimeSelect = document.getElementById('break-time');
            const setCountSelect = document.getElementById('set-count');
            const workTime = parseInt(workTimeSelect.options[workTimeSelect.selectedIndex].value);
            const breakTime = parseInt(breakTimeSelect.options[breakTimeSelect.selectedIndex].value);
            const setCount = parseInt(setCountSelect.options[setCountSelect.selectedIndex].value);

            // APIエンドポイントURLを設定
            const apiUrl = 'http://127.0.0.1:5000'; // 実際のエンドポイントURLに置き換えてください

            // リクエストボディを作成
            const requestData = {
                user_data: {
                concerns: concernsArray,
                work_time: workTime,
                break_time: breakTime,
                set_count: setCount,
                },
            };
            var msg = {
                'option' : 'setting', 
                'concerns': concernsArray,
                'work_time': workTime,
                'break_time': breakTime,
                'set_count': setCount,
            }
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
                console.log(message);
                //messageTextArea.value += "Receive => "+message.data+"\n";
            };
            

            try {
            // axiosを使ってAPIエンドポイントにPOSTリクエストを送信
            const response = await axios.post(apiUrl, requestData);
            const responseData = response.data;

            // レスポンスデータを表示（確認用）
            console.log(responseData);
            
            // ここで取得したデータを使って必要な処理を行う
            // 例: レスポンスデータをVueコンポーネント内で使用する場合

        } catch (error) {
            console.error('APIリクエストエラー:', error);
        }

            this.setWorkTime(workTime);
            this.setBreakTime(breakTime);
            this.setSetCount(setCount);
            this.$router.push('/firsttimer');
        }
    },
    mounted() {
        const options = document.querySelectorAll('.option');

        options.forEach(option => {
            option.addEventListener('click', () => {
                option.classList.toggle('selected');
            });
        });
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
    background-color: #999;
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
