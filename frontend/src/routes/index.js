import { createRouter, createWebHistory } from "vue-router";
import { users } from "./users_routes.js";
import { roles } from "./roles_routes.js";
import { auth_routes } from "./auth_routes.js";
import { useAuthStore } from "../storage/auth.js";
import { exercises } from "./exercises_routes.js";

const routes = [{
    path: "/",
    name: "Home",
    component: () => import("../views/HomeView.vue"),
    meta: {
        rol_access: ["admin", "operador"],
        required_auth: true,
        orden: 10,
        menu: true
    }
}, ...auth_routes, ...users, ...roles, ...exercises];

export const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach((to, from) => {
    const authStore = useAuthStore()
    if (to.meta.rol_access && !authStore.authenticated && to.name !== 'Login') {
        return { name: "Login" }; 
    }
    if (to.meta.rol_access && !to.meta.rol_access.includes(authStore.rol_user) && to.name !== 'Home') {
        return { name: "Home" }
    }
})