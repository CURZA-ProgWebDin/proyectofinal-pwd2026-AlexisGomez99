export const roles = [{
    path: "/roles",
    name: "Roles",
    component: () => import("../views/RolesView.vue"),
    meta: {
        rol_access: ["admin","entrenador"],
        required_auth: true,
        orden: 900,
        menu: true
    }
},
{
    path: "/roles/create",
    component: () => import("../components/roles/RolesCreate.vue"),
    name: "RolesCreate",
    meta: {
        rol_access: ["admin"],
        required_auth: true,
        orden: 901,
        menu: false
    }
},
{
    path: "/roles/edit",
    component: () => import("../components/roles/RolesEdit.vue"),
    name: "RolesEdit",
    meta: {
        rol_access: ["admin"],
        required_auth: true,
        orden: 902,
        menu: false
    }
}
]