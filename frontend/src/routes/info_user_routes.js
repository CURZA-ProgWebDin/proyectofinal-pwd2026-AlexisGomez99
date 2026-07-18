export const my_account = [{
    path: "/my_account",
    name: "MyAccount",
    component: () => import("../components/auth/MyAccount.vue"),
    meta: {
        rol_access: ["admin", "operador", "entrenador", "creador"],
        required_auth: true,
        orden: 11,
        menu: false
    }
},
{
    path: "/my_account/create",
    component: () => import("../components/auth/InfoUsersCreate.vue"),
    name: "InfoUsersCreate",
    meta: {
        rol_access: ["admin", "operador", "entrenador", "creador"],
        required_auth: true,
        orden: 12,
        menu: false
    }
},{
    path: "/my_account/edit",
    component: () => import("../components/auth/InfoUsersEdit.vue"),
    name: "InfoUsersEdit",
    meta: {
        rol_access: ["admin", "operador", "entrenador", "creador"],
        required_auth: true,
        orden: 13,
        menu: false
    }
}];

