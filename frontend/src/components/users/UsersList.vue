<script setup>
import { onMounted, ref, computed } from "vue";
import { useUserStore } from "../../storage/users.js";
import { storeToRefs } from "pinia";
import DataTable from "../DataTable.vue";
import { mdiCone } from "@mdi/js";
import { useRouter } from "vue-router";

const userStore = useUserStore();
const { listUsers, destroy } = userStore;
const router = useRouter();
const { users } = storeToRefs(userStore);
const { setUser } = userStore; 
const loading = ref(true);
const list_users = computed(() => {
    if (users.value.length === 0) {
        return [];
    } else {
        return users.value.map((user) => {
            return {
                id: user.id,
                name: user.name,
                email: user.email,
                active: user.active ? "activo" : "inactivo",
                rol_id: user.rol.id,
                rol: user.rol.name
            };
        });
    }
});
async function eliminarUsuario(user) {
    loading.value= true;
    await destroy(user.id);
    await listUsers();
    loading.value= false;
}
function editarUsuario(user) {
    setUser(user)
    router.push({ name: 'UsersEdit' });
}
onMounted(() => {
    listUsers();
    loading.value=false
});
</script>

<template>
    <section class="admin-section">
        <div class="header-container">
            <h3>
                <mdicon name="account" class="icon-title"></mdicon>
                Lista de Usuarios
            </h3>

            <RouterLink :to="{ name: 'UsersCreate' }" class="nav-link">
                <button class="btn-primary">
                    <mdicon name="account-plus"></mdicon>
                    <span>Crear usuario</span>
                </button>
            </RouterLink>
        </div>
        
        <template v-if="list_users.length === 0">
            <div class="empty-state">
                <p>No se encontraron usuarios en la base de datos.</p>
            </div>
        </template>


        <div v-else class="table-container">
            <DataTable v-if="!loading" :data="list_users" :headers="['ID', 'NAME', 'EMAIL', 'ROL', 'ACTIVE']" class="custom-table"
                @eliminar="eliminarUsuario" @editar="editarUsuario" />

            <p v-else >"Cargando..."</p>
        </div>
    </section>
</template>

<style scoped>
.admin-section {
    background-color: #0f172a;
    min-height: 100vh;
    padding: 2.5rem;
    color: #f8fafc;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    box-sizing: border-box;
}


.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
    border-bottom: 1px solid #334155;
    padding-bottom: 1.2rem;
}

h3 {
    margin: 0;
    font-size: 1.6rem;
    font-weight: 600;
    letter-spacing: 1px;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    color: #f8fafc;
}

.icon-title {
    color: #10b981;
}

.nav-link {
    text-decoration: none;
}


.btn-primary {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.25rem;
    font-size: 0.95rem;
    font-weight: 700;
    color: #0f172a;
    background-color: #10b981;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.15);
    transition: background-color 0.2s ease, transform 0.1s ease, box-shadow 0.2s ease;
}

.btn-primary:hover {
    background-color: #059669;
    box-shadow: 0 6px 16px rgba(16, 185, 129, 0.25);
}

.btn-primary:active {
    transform: scale(0.98);
}


.empty-state {
    background-color: #1e293b;
    border: 1px dashed #475569;
    border-radius: 8px;
    padding: 3rem;
    text-align: center;
    color: #94a3b8;
    font-size: 1.1rem;
}


.table-container {
    background-color: #1e293b;
    border-radius: 8px;
    border: 1px solid #334155;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    overflow-x: auto;
    padding: 1rem;
}


.custom-table :deep(table) {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
    font-size: 0.95rem;
}


.custom-table :deep(th) {
    background-color: #0f172a;
    color: #94a3b8;
    padding: 1rem;
    font-weight: 700;
    font-size: 0.85rem;
    letter-spacing: 0.5px;
    border-bottom: 2px solid #334155;
}


.custom-table :deep(td) {
    padding: 1rem;
    border-bottom: 1px solid #334155;
    color: #e2e8f0;
}


.custom-table :deep(tr:hover td) {
    background-color: #243249;
    color: #f8fafc;
    transition: background-color 0.15s ease;
}
</style>