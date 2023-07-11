<template>
    <div class="FeedBack">

        <div class="comment1">今回のストレッチはどうでしたか？</div>
        <div class="StretchFB">
            <div class="Stretch"></div>
            <div class="FB">
                <div class="icon-wrapper">
                    <ThumbUpOutline :size="24" />        
                </div>
                <div class="icon-spacing"></div>
                <div class="icon-wrapper">
                    <ThumbDownOutline :size="24" />
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
        ThumbDownOutline
    }
}


</script>


<style scoped>
.FeedBack{
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: #FFFBEC;
  background-image: url("./pattern-image.png");
  background-repeat: no-repeat;
  background-size: cover;
}

.comment1{
    text-align: center;
    margin-top: 120px;
    color: #382823;
    font-weight:bold;
    font-size: 20px;
}

.Stretch{
    text-align: center;
    width: 160px;
	height: 160px;
	border-radius: 50%;
    background: #E5F3E7;
    margin-top: 90px;
    margin-left: auto;
    margin-right: auto;
}

.StretchFB{
    text-align: center;
}

.FB {
  display: flex;
  justify-content: center;
}

.icon-wrapper {
  margin: 10px; /* 余白の幅を調整してください */
  cursor: pointer;
  color: #737373;
}

.comment2{
    text-align: center;
    margin-top: 150px;
    color: #382823;
    font-weight:bold;
    font-size: 20px;
}

.backbutton{
    width: 120px;
    height: 40px;
    border-radius: 20px;
    background: #4FA095;
    margin-top: 40px;
    margin-left: auto;
    margin-right: auto;
    cursor: pointer;
    box-shadow: 0 0 5px #737373;
}

.backtext{
    font-weight:bold;
    text-align: center;
    padding-top: 7px;
    color: #FFFBEC;
}
</style>