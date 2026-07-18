<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter, useRoute } from "vue-router";
import { storeToRefs } from "pinia";
import { useRoutineStore } from "../../storage/routines";
import { useUserStore } from "../../storage/users";

const router = useRouter();
const route = useRoute();
const routineStore = useRoutineStore();
const userStore = useUserStore();

const { users } = storeToRefs(userStore);
const { listUsers } = userStore;
const { routineEdit } = storeToRefs(routineStore);
const { update, getOne } = routineStore;

const loading = ref(true);
const searchQuery = ref("");

onMounted(async () => {
    try {
        await listUsers();
        const routineId = route.params.id;
        if (routineId) {
            await getOne(routineId);
        }
    } catch (error) {
        console.error("Error al cargar la rutina para editar:", error);
    } finally {
        loading.value = false;
    }
});

const filteredUsers = computed(() => {
    if (!searchQuery.value.trim()) return users.value;
    const query = searchQuery.value.toLowerCase();
    return users.value.filter(user => user.name?.toLowerCase().includes(query));
});

function seleccionarUsuario(user) {
    if (routineEdit.value) {
        routineEdit.value.user_id = user.id;
        if (!routineEdit.value.user) routineEdit.value.user = {};
        routineEdit.value.user.name = user.name;
    }
}

async function editar() {
    await update(routineEdit.value);
    router.push({ name: 'Routines' });
}
</script>

<template>
    <div class="edit-routine-page">
        <div v-if="loading" class="loading-state">
            <p>Cargando datos...</p>
        </div>

        <div v-else class="flex-layout">
            <div class="form-column">
                <div v-if="routineEdit" class="form-card">
                    <form @submit.prevent="editar" class="custom-form">
                        <button type="button" @click="router.push({ name: 'Routines' })" class="cancel-btn" title="Cancelar">
                            <mdicon name="close" size="18"></mdicon>
                        </button>

                        <h2>Editar rutina</h2>

                        <div class="form-group">
                            <label>NOMBRE DE LA RUTINA</label>
                            <input type="text" v-model="routineEdit.name" required>
                        </div>

                        <div class="form-group">
                            <label>USUARIO ASIGNADO</label>
                            <input 
                                type="text"
                                :value="routineEdit.user ? (routineEdit.user.name || routineEdit.user) : 'Ninguno seleccionado'"
                                disabled 
                                class="disabled-input"
                            >
                        </div>

                        <button type="submit" class="submit-btn" :disabled="!routineEdit.user_id">
                            ACEPTAR CAMBIOS
                        </button>
                    </form>
                </div>

                <div v-else class="form-card loading-card">
                    <p class="loading-text">Cargando datos de la rutina...</p>
                </div>
            </div>

            <div class="selector-column">
                <div class="selector-container">
                    <h3>Asignar Usuario</h3>

                    <div class="search-bar">
                        <mdicon name="magnify" size="18" class="search-icon"></mdicon>
                        <input 
                            type="text" 
                            v-model="searchQuery" 
                            placeholder="Buscar usuario por nombre..."
                            class="search-input"
                        >
                    </div>

                    <div class="table-wrapper-mini">
                        <table class="selector-table">
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>NOMBRE</th>
                                    <th>ACCION</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr 
                                    v-for="user in filteredUsers" 
                                    :key="user.id"
                                    :class="{ 'selected-row': routineEdit?.user_id === user.id }"
                                >
                                    <td>{{ user.id }}</td>
                                    <td>{{ user.name }}</td>
                                    <td>
                                        <button 
                                            type="button" 
                                            class="btn-select" 
                                            @click="seleccionarUsuario(user)"
                                            :class="{ 'btn-selected': routineEdit?.user_id === user.id }"
                                        >
                                            {{ routineEdit?.user_id === user.id ? 'Asignado' : 'Asignar' }}
                                        </button>
                                    </td>
                                </tr>
                                <tr v-if="filteredUsers.length === 0">
                                    <td colspan="3" class="no-results">No se encontraron usuarios</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.edit-routine-page {
    background-color: #0f172a;
    min-height: 100vh;
    padding: 40px 20px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    box-sizing: border-box;
    display: flex;
    justify-content: center;
    align-items: center;
}

.flex-layout {
    display: flex;
    gap: 30px;
    max-width: 1000px;
    width: 100%;
    margin: 0 auto;
    align-items: stretch; 
}

.form-column,
.selector-column {
    flex: 1;
    min-width: 320px;
    display: flex;
    flex-direction: column;
}

.form-card,
.selector-container {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    padding: 30px;
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
}

.custom-form {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
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

h3 {
    margin-top: 0;
    margin-bottom: 24px;
    color: #f8fafc;
    font-size: 20px;
    font-weight: 600;
    letter-spacing: 1px;
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

input[type="text"] {
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

input:focus {
    border-color: #10b981;
    box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.15);
}

.disabled-input {
    background-color: #1e293b !important;
    border: 1px solid #334155 !important;
    color: #64748b !important;
    cursor: not-allowed;
}

.search-bar {
    display: flex;
    align-items: center;
    background-color: #0f172a;
    border: 1px solid #475569;
    border-radius: 6px;
    padding: 2px 12px;
    margin-bottom: 20px;
    transition: border-color 0.3s;
}

.search-bar:focus-within {
    border-color: #10b981;
    box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.15);
}

.search-icon {
    color: #64748b;
    margin-right: 8px;
    display: flex;
    align-items: center;
}

.search-input {
    border: none !important;
    background: transparent !important;
    color: #f8fafc !important;
    width: 100%;
    outline: none;
    font-size: 14px;
    padding: 10px 0 !important;
}

.table-wrapper-mini {
    max-height: 250px;
    overflow-y: auto;
    border: 1px solid #334155;
    border-radius: 6px;
    background-color: #0f172a;
}

.selector-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    text-align: left;
}

.selector-table th,
.selector-table td {
    padding: 12px;
    border-bottom: 1px solid #334155;
    color: #cbd5e1;
}

.selector-table th {
    background-color: #1e293b;
    color: #94a3b8;
    font-weight: 700;
    position: sticky;
    top: 0;
    z-index: 1;
}

/* Fila activa */
.selected-row {
    background-color: rgba(16, 185, 129, 0.1) !important;
}

.selected-row td {
    color: #10b981;
    font-weight: 600;
}

/* Botón seleccionar */
.btn-select {
    background-color: transparent;
    border: 1px solid #10b981;
    color: #10b981;
    padding: 6px 12px;
    font-size: 12px;
    font-weight: 700;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s ease;
    width: 100%;
    text-transform: uppercase;
}

.btn-select:hover {
    background-color: #10b981;
    color: #0f172a;
}

.btn-selected {
    background-color: #10b981 !important;
    color: #0f172a !important;
}

/* Estados de carga y vacíos */
.no-results {
    text-align: center;
    color: #64748b;
    padding: 20px !important;
}

.loading-state {
    color: #f8fafc;
    text-align: center;
    padding: 40px;
    font-size: 18px;
}

.loading-card {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 334px; /* Altura promedio del formulario */
}

.loading-text {
    color: #94a3b8;
    font-size: 14px;
}

/* Botones Principales */
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

.submit-btn:hover:not(:disabled) {
    background-color: #059669;
}

.submit-btn:disabled {
    background-color: #1e293b;
    color: #475569;
    border: 1px solid #334155;
    cursor: not-allowed;
    box-shadow: none;
}

.submit-btn:active:not(:disabled) {
    transform: scale(0.98);
}

.cancel-btn {
    position: absolute;
    top: -10px;
    right: -10px;
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
    z-index: 10;
}

.cancel-btn:hover {
    background-color: #dc2626;
}

.cancel-btn:active {
    transform: scale(0.92);
}

/* Responsividad */
@media (max-width: 850px) {
    .flex-layout {
        flex-direction: column;
        align-items: center;
    }

    .form-column,
    .selector-column {
        width: 100%;
        max-width: 450px;
    }

    .cancel-btn {
        top: 16px;
        right: 16px;
    }
}
</style>