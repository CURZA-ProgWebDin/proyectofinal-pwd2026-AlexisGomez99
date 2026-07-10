<template>
  <section>
    <transition name="slide" mode="out-in">
      <div id="notificacion" v-if="visible" :class="notification_type">
        <p>
          <mdicon :name="notification_icons[notification_type]"></mdicon
          >{{ message }}
        </p>
        <mdicon name="close" @click="visible = false"></mdicon>
      </div>
    </transition>
  </section>
</template>
<script setup>
import { storeToRefs } from "pinia";
import { watch } from "vue";
import { useNotificationStore } from "../storage/notifications";

const notification_icons = {
  success: "check-circle",
  info: "information",
  error: "alert-circle",
  warning: "alert",
};
const store = useNotificationStore();
const { message, visible, timer, notification_type } = storeToRefs(store);
let timeoutId = null;

watch(
  () => visible.value,
  (nuevo_valor) => {
    if (nuevo_valor) {
      if (timeoutId) clearTimeout(timeoutId);

      timeoutId = setTimeout(() => {
        visible.value = false;
      }, timer.value);
    }
  },
);
</script>
<style scoped>
section {
  display: flex;
  justify-content: center;
}
#notificacion {
  position: absolute;
  text-align: center;
  z-index: 99;
  width: 50%;
  border-radius: 10px;
  padding: 10px 20px;
  top: 10px;
  color: #fff;
  font-size: 18px;
  display: flex;
  justify-content: center;
}

.success {
  background-color: rgb(27, 216, 68);
}

.error {
  background-color: rgb(185, 7, 7);
}

.warning {
  background-color: rgb(255, 153, 0);
}
.info {
  background-color: rgb(6, 216, 231);
}
/** transicion  animada  */
.slide-enter-from,
.slide-leave-to {
  transform: translateY(-80px);
}
.slide-enter-active {
  transition: all 0.5s cubic-bezier(1, 0.5, 0.8, 1);
}
</style>