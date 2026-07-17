<script setup>
import { onMounted, ref, computed } from "vue";
import { useUserStore } from "../../storage/users.js";
import { storeToRefs } from "pinia";
import DataTable from "../DataTable.vue";
import { mdiCone } from "@mdi/js";
import { useRouter } from "vue-router";
import { useRoutineStore } from "../../storage/routines.js";

const props = defineProps({
    user_id: {
        type: [String, Number, null],
        default: null
    }
});

const RoutineStore = useRoutineStore();
const { listRoutines, destroy } = RoutineStore;
const router = useRouter();
const { routines } = storeToRefs(RoutineStore);
const { setRoutine } = RoutineStore;
const loading = ref(true);
const list_routines = computed(() => {
    if (routines.value.length === 0) {
        return [];
    }

    const mappedRoutines = routines.value.map((routine) => {
        return {
            id: routine.id,
            name: routine.name,
            user: routine.user ? (routine.user.name || routine.user) : 'Sin asignar',
            user_id: routine.user ? routine.user.id : null,
            created_at: routine.created_at
        };
    });
    if (props.user_id) {
        return mappedRoutines.filter(routine => routine.user_id === Number(props.user_id));
    }

    return mappedRoutines;
});
async function deleteRoutine(routine) {
    loading.value = true;
    await destroy(routine.id);
    await listRoutines();
    loading.value = false;
}
function editRoutine(routine) {
    setRoutine(routine)
    router.push({
        name: 'RoutinesEdit',
        params: { id: routine.id }
    });
}
function getExercisesForWeek(id){
    router.push({
        name: 'InfoRoutinesWeek',
        params: { id: id }
    });
}
onMounted(() => {
    listRoutines();
    loading.value = false
});
</script>

<template>
    <section class="admin-section">
        <div class="header-container">
            <h3>
                <mdicon name="account" class="icon-title"></mdicon>
                Lista de Rutinas
            </h3>

            <RouterLink :to="{ name: 'RoutinesCreate' }" class="nav-link">
                <button class="btn-primary">
                    <mdicon name="account-plus"></mdicon>
                    <span>Crear rutina</span>
                </button>
            </RouterLink>
        </div>

        <template v-if="list_routines.length === 0">
            <div class="empty-state">
                <p>No se encontraron rutinas en la base de datos.</p>
            </div>
        </template>


        <div v-else class="table-container">
            <DataTable v-if="!loading" :data="list_routines" :headers="['ID', 'NAME', 'USER', 'CREATED_AT']"
                class="custom-table" @eliminar="deleteRoutine" @editar="editRoutine">
                <template #acciones-extra="{ id }">
                    <button class="btn btn-info" @click="getExercisesForWeek(id)" title="Ver esta Rutina">
                        <mdicon name="eye" size="18"></mdicon>
                    </button>
                </template>
            </DataTable>

            <p v-else>"Cargando..."</p>
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

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: none;
  cursor: pointer;
  padding: 6px;
  border-radius: 4px;
  margin: 0 4px;
  transition: background-color 0.2s ease, transform 0.1s ease;
  color: #ffffff;
}

.btn-info {
  background-color: #17a2b8;
}
.btn-info:hover {
  background-color: #138496;
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