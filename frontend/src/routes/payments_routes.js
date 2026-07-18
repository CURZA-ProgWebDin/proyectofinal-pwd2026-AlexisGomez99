export const payments = [{
    path: "/payments",
    name: "Payments",
    component: () => import("../views/PaymentsView.vue"),
    meta: {
        rol_access: ["admin","entrenador"],
        required_auth: true,
        orden: 600,
        menu: true
    }
},
{
    path: "/payments/create",
    component: () => import("../components/payments/PaymentsCreate.vue"),
    name: "PaymentsCreate",
    meta: {
        rol_access: ["admin","entrenador"],
        required_auth: true,
        orden: 601,
        menu: false
    }
},{
    path: "/payments/edit",
    component: () => import("../components/payments/PaymentsEdit.vue"),
    name: "PaymentsEdit",
    meta: {
        rol_access: ["admin"],
        required_auth: true,
        orden: 602,
        menu: false
    }
}];

