<script setup>
import { computed, onMounted, reactive } from "vue";
import { useRoute, useRouter } from "vue-router";
import { storeToRefs } from "pinia";
import { useRolesStore } from "../../storage/roles";
import { useAuthStore } from "../../storage/auth";

const rolStore = useRolesStore();
const authStore = useAuthStore();
const { roles } = storeToRefs(rolStore);
const { list } = rolStore;
const { register } = authStore;
const route = useRoute();
const router = useRouter();
const new_user = reactive({
    name: "",
    email: "",
    rol_id: 2,
    password: ""
});

async function submit() {
    if (new_user.name && new_user.email && new_user.password && new_user.rol_id) {
        await register(new_user);
        new_user.name = "";
        new_user.email = "";
        new_user.password = "";
        router.push({ name: "Login" });
    } else {
        alert("Complete todos los campos.");
    }
}
</script>

<template>
    <div class="form-container">
        <form @submit.prevent="submit" class="custom-form">
            <h2>Registrarme</h2>

            <div class="form-group">
                <label>NOMBRE</label>
                <input type="text" v-model="new_user.name" placeholder="Ej: Alexis Gómez">
            </div>

            <div class="form-group">
                <label>EMAIL</label>
                <input type="email" v-model="new_user.email" placeholder="correo@ejemplo.com">
            </div>

            <div class="form-group">
                <label>CONTRASEÑA</label>
                <input type="password" v-model="new_user.password" placeholder="••••••••">
            </div>

            <button type="submit" class="submit-btn">
                REGISTRARME
            </button>
        </form>
    </div>
</template>

<style scoped>
.form-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 20px;
    background-color: #0f172a;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    box-sizing: border-box;
}

.custom-form {
    background: #1e293b;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    width: 100%;
    max-width: 400px;
    box-sizing: border-box;
    border: 1px solid #334155;
}


h2 {
    margin-top: 0;
    margin-bottom: 24px;
    color: #f8fafc;
    text-align: center;
    font-size: 24px;
    font-weight: 600;
    letter-spacing: 1.5px;
}

.form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
}


label {
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 6px;
    color: #94a3b8;
    letter-spacing: 0.5px;
}


input[type="text"],
input[type="email"],
input[type="password"],
select {
    padding: 12px;
    border: 1px solid #475569;
    border-radius: 6px;
    font-size: 14px;
    color: #f8fafc;
    background-color: #0f172a;
    transition: all 0.3s ease;
    outline: none;
    width: 100%;
    box-sizing: border-box;
}


input::placeholder {
    color: #64748b;
}


input:focus,
select:focus {
    border-color: #10b981;
    background-color: #0f172a;
    box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.15);
}


.submit-btn {
    width: 100%;
    padding: 14px;
    background-color: #10b981;
    color: #0f172a;
    border: none;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.5px;
    cursor: pointer;
    transition: background-color 0.2s ease, transform 0.1s ease;
    margin-top: 10px;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2);
}


.submit-btn:hover {
    background-color: #059669;
}

.submit-btn:active {
    transform: scale(0.98);
}
</style>