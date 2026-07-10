import { defineStore } from "pinia";
import { ref } from "vue";

export const useNotificationStore = defineStore("notificacion", () => {
  const message = ref("");
  const visible = ref(false);
  const notification_type = ref("");
  const timer = ref(0);

  function create(mnsaje, visibilidad, tipo = "success", tiempo = 3000) {
    message.value = mnsaje;
    visible.value = visibilidad;
    notification_type.value = tipo;
    timer.value = tiempo;
  }

  return { message, visible, notification_type, timer, create };
});