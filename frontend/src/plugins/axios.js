import axios from "axios";
import { useAuthStore } from "../storage/auth";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";
import { useNotificationStore } from "../storage/notifications";

export const instance = axios.create({
  baseURL: "http://localhost:5001/api_v1/",
  timeout: 5000,
});

export const instance_auth = axios.create({
  baseURL: "http://localhost:5001/api_v1/",
  timeout: 5000,
});

instance_auth.interceptors.request.use(function (config) {
  const authStore = useAuthStore();
  const { jwt } = storeToRefs(authStore);
  if (jwt.value) {
    config.headers.Authorization = `Bearer ${jwt.value}`;
  }
  return config;
});
instance_auth.interceptors.response.use(
  (response) => {
    const notificationStore = useNotificationStore();
    const authStore = useAuthStore();
    const { jwt } = storeToRefs(authStore);
    if (response.data.refresh_token) {
      const authStore = useAuthStore();
      jwt.value = response.data.refresh_token;
    }
    if (response.data.message) {
      notificationStore.create(response.data.message, true);
    }

    return response.data;
  },
  (error) => {
    const authStore = useAuthStore();
    const notificationStore = useNotificationStore();
    
    const status = error.response?.status;
    const backendMessage = error.response?.data?.message;

    if (backendMessage) {
      notificationStore.create(backendMessage, true, "error");
    }

    if (status === 401) {
      authStore.logout();
    }
    
    if (status === 409) {
      notificationStore.create(backendMessage || "Conflicto", true, "warning");
    }

    if (status === 403) {
      authStore.goHome();
    }

    return Promise.reject(error);
  }
);