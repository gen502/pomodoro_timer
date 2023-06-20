<template>
    <div class="container">
        <h1>タイマー設定</h1>
        <form>
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

            <label for="body-part">体の悩み:</label>
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
</template>

<script>
export default {
    name: 'SettingVue',
    mounted() {
        const options = document.querySelectorAll('.option');

        options.forEach(option => {
            option.addEventListener('click', () => {
                option.classList.toggle('selected');
            });
        });
    }
}
</script>

<style scoped>
.container {
    max-width: 500px;
    margin: auto;
    text-align: center;
}

h1 {
    margin-top: 50px;
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
