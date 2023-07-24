<template>
    <div class="setting" style="color: white;">
        <CogIcon :size="23" style="margin-right: 2px; margin-top: 5px;" />
    </div>
</template>

<script>
import CogIcon from "vue-material-design-icons/Cog.vue";

export default {
    components: {
        CogIcon,
    }
}    

</script>

<style scoped>
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

</style>