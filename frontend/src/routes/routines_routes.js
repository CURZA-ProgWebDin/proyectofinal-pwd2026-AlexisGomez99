export const routines = [{
    path: "/routines",
    name: "Routines",
    component: () => import("../views/RoutinesView.vue"),
    meta: {
        rol_access: ["admin","entrenador","creador"],
        required_auth: true,
        orden: 500,
        menu: true
    }
},
{
    path: "/routines/create",
    component: () => import("../components/routines/RoutinesCreate.vue"),
    name: "RoutinesCreate",
    meta: {
        rol_access: ["admin","entrenador","creador"],
        required_auth: true,
        orden: 501,
        menu: false
    }
},{
    path: "/routines/edit/:id",
    component: () => import("../components/routines/RoutinesEdit.vue"),
    name: "RoutinesEdit",
    meta: {
        rol_access: ["admin","entrenador","creador"],
        required_auth: true,
        orden: 502,
        menu: false
    }
}];

