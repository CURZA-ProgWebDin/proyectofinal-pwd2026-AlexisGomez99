export const exercises = [{
    path: "/exercises",
    name: "Exercises",
    component: () => import("../views/ExercisesView.vue"),
    meta: {
        rol_access: ["admin","entrenador"],
        required_auth: true,
        orden: 700,
        menu: true
    }
},
{
    path: "/exercises/create",
    component: () => import("../components/exercises/ExercisesCreate.vue"),
    name: "ExercisesCreate",
    meta: {
        rol_access: ["admin","entrenador"],
        required_auth: true,
        orden: 701,
        menu: false
    }
},
{
    path: "/exercises/edit",
    component: () => import("../components/exercises/ExercisesEdit.vue"),
    name: "ExercisesEdit",
    meta: {
        rol_access: ["admin","entrenador"],
        required_auth: true,
        orden: 702,
        menu: false
    }
}
]