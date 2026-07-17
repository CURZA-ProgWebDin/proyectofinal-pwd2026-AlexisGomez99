import AuthService from "../service/AuthService";
import { defineStore } from "pinia";
import { ref } from "vue";
import { router } from "../routes";
import { useRouter } from "vue-router";

export const useAuthStore = defineStore("auth", () => {
    const auth_user = ref(null);
    const id = ref(null);
    const rol_user = ref("");
    const authenticated = ref(false);
    const jwt = ref("");
    const router = useRouter();
    const service = new AuthService();
    const errors = ref([]);
    const status_code = ref(null);

    async function login(user) {
        auth_user.value = await service.login(user);
        auth_user.value = service.auth_user.name;
        id.value = service.auth_user.id;
        authenticated.value = service.auth_user.authenticated;
        jwt.value = service.auth_user.access_token;
        rol_user.value = service.auth_user.rol;
    }
    function logout() {
        auth_user.value = null;
        jwt.value = "";
        authenticated.value = false;
        rol_user.value = "";
    }
    async function register(new_user) {
        const response = await service.register(new_user);
        if (response) {
            status_code.value = response;
        }
    }
    async function getMe() {
        const data = await api_service.findOne(auth_user.id);
        if (data) {
            auth_user.value = data;
        }
    }
    function goHome() {
      router.push("/");
    }
    return {
        auth_user, rol_user, jwt, id,errors, status_code, authenticated, login, logout, register, getMe, goHome
    }
}, {
    persist: true
});