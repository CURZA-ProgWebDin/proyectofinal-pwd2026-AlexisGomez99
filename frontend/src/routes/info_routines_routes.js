export const info_routines = [{
    path: "/info_routines",
    name: "InfoRoutines",
    component: () => import("../views/UserRoutinesView.vue"),
    meta: {
        rol_access: ["admin", "operador", "entrenador", "creador"],
        required_auth: true,
        orden: 400,
        menu: false
    }
},{
    path: "/info_routines/week/:id",
    name: "InfoRoutinesWeek",
    component: () => import("../components/info_routines/RoutinesWeek.vue"),
    meta: {
        rol_access: ["admin", "operador", "entrenador", "creador"],
        required_auth: true,
        orden: 401,
        menu: false
    }
},{
    path: "/info_routines/week/edit/:id",
    name: "InfoRoutinesWeekEdit",
    component: () => import("../components/info_routines/RoutineEdit.vue"),
    meta: {
        rol_access: ["admin", "operador", "entrenador", "creador"],
        required_auth: true,
        orden: 402,
        menu: false
    }
}];

