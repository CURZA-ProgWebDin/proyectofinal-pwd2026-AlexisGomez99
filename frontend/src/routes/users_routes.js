export const users = [{
    path: "/usuarios",
    name: "Users",
    component: () => import("../views/UsersView.vue"),
    meta: {
        rol_access: ["admin","entrenador","creador"],
        required_auth: true,
        orden: 800,
        menu: true
    }
},
{
    path: "/usuarios/create",
    component: () => import("../components/users/UsersCreate.vue"),
    name: "UsersCreate",
    meta: {
        rol_access: ["admin","entrenador"],
        required_auth: true,
        orden: 801,
        menu: false
    }
},{
    path: "/usuarios/edit",
    component: () => import("../components/users/UsersEdit.vue"),
    name: "UsersEdit",
    meta: {
        rol_access: ["admin"],
        required_auth: true,
        orden: 802,
        menu: false
    }
}];

