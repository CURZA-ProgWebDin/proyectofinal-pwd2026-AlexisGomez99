<script setup>
import { useRouter } from 'vue-router';
import { onMounted, reactive, ref } from 'vue';
import { storeToRefs } from 'pinia';
import { useRoutineStore } from '../../storage/routines';
import { useInfoUserStore } from '../../storage/infousers';

const router = useRouter();
const infouserStore = useInfoUserStore();
const { infoUserEdit } = storeToRefs(infouserStore);
const { update } = infouserStore;
const loading = ref(true);

onMounted(async () => {
    loading.value = false;
})

async function editar() {
    await update(infoUserEdit.value);
    router.push({ name: 'MyAccount' })
}
</script>

<template>
    <div class="form-container">
        <form @submit.prevent="editar" class="custom-form">

            <button type="button" @click="router.push({ name: 'MyAccount' })" class="cancel-btn" title="Cancelar">
                <mdicon name="close" size="18"></mdicon>
            </button>

            <h2>Editar perfil</h2>

            <div class="form-group">
                <label>NOMBRE</label>
                <input type="text" v-model="infoUserEdit.name">
            </div>
            <div class="form-group">
                <label>APELLIDOS</label>
                <input type="text" v-model="infoUserEdit.last_name">
            </div>
            <div class="form-group">
                <label>DNI</label>
                <input type="text" v-model="infoUserEdit.dni">
            </div>
            <div class="form-group">
                <label>DIRECCION</label>
                <input type="text" v-model="infoUserEdit.number_phone">
            </div>
            <div class="form-group">
                <label>NUMERO DE TELEFONO</label>
                <input type="text" v-model="infoUserEdit.adress">
            </div>
            <button type="submit" class="submit-btn">
                ACEPTAR CAMBIOS
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
    position: relative;
    background: #1e293b;
    padding: 40px 30px 30px 30px;
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


.cancel-btn {
    position: absolute;
    top: 16px;
    right: 16px;
    width: 32px;
    height: 32px;
    padding: 0;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background-color: #ef4444;
    color: #f8fafc;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(239, 68, 68, 0.25);
    transition: background-color 0.2s ease, transform 0.1s ease;
}

.cancel-btn:hover {
    background-color: #dc2626;
}

.cancel-btn:active {
    transform: scale(0.92);
}
</style>