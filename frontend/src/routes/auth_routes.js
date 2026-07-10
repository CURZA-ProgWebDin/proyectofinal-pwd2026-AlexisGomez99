export const auth_routes = [
    {
        path: "/login",
        component: () => import("../views/LoginView.vue"),
        name: "Login",
        meta: {
            required_auth: false,
            orden: 2,
            menu: true
        }
    }, {
        path: "/register",
        component: () => import("../views/RegisterView.vue"),
        name: "Register",
        meta: {
            required_auth: false,
            orden: 2,
            menu: true
        }
    }
];