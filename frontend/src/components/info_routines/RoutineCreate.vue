<script setup>
import { computed, onMounted, reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { storeToRefs } from "pinia";
import { useInfoRoutineStore } from "../../storage/inforoutines";
import { useExerciseStore } from "../../storage/exercises";

const infoRoutineStore = useInfoRoutineStore();
const exerciseStore = useExerciseStore();
const { exercises } = storeToRefs(exerciseStore);
const { listExercises } = exerciseStore;
const { create } = infoRoutineStore;
const router = useRouter();
const route = useRoute();

const searchQuery = ref("");
const loading = ref(true);
const new_inforoutine = reactive({
    day: "",
    comment: "",
    description: "",
    name_section: "",
    sets: "",
    reps: "",
    weights: "",
    routine_id: "",
    exercise_id: ""
});

onMounted(async () => {
    await listExercises();
})
async function submit() {
    if (new_inforoutine.day && new_inforoutine.name_section && new_inforoutine.exercise_id) {
        new_inforoutine.name_section = new_inforoutine.name_section.toUpperCase();
        new_inforoutine.routine_id = route.params.id; 
        await create(new_inforoutine);
        new_inforoutine.day = "";
        new_inforoutine.name_section = "";
        new_inforoutine.exercise_id = "";
        new_inforoutine.routine_id = "";
        router.back();

    } else {
        alert("Complete todos los campos.");
    }
}

function selecExercise(exercise) {
    new_inforoutine.exercise_id = exercise.id;
}
const filteredExercises = computed(() => {
    if (!searchQuery.value.trim()) return exercises.value;
    const query = searchQuery.value.toLowerCase();
    return exercises.value.filter(exercise => exercise.name?.toLowerCase().includes(query));
});
</script>

<template>
    <div class="routine-manager-container">
        <form @submit.prevent="submit" class="routine-form-card">

            <button type="button" @click="router.back()" class="close-floating-btn" title="Cancelar">
                <mdicon name="close" size="20"></mdicon>
            </button>

            <h2 class="form-main-title">Agregar ejercicio</h2>

            <div class="day-selector-group">
                <span class="group-label">DÍA</span>
                <div class="days-radio-container">
                    <label v-for="day in ['LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES', 'SABADO', 'DOMINGO']"
                        :key="day" class="day-radio-label">
                        <input type="radio" :value="day" v-model="new_inforoutine.day" class="day-radio-input" />
                        <span class="day-radio-btn">{{ day }}</span>
                    </label>
                </div>
            </div>

            <div class="split-layout-container">
                <div class="exercise-selector-panel">
                    <div class="form-field-group">
                        <label>NOMBRE DE LA SECCION</label>
                        <input type="text" v-model="new_inforoutine.name_section" placeholder="Ej. ESPALDA" required>
                    </div>
                    <h3 class="panel-subtitle">Asignar Ejercicio</h3>

                    <div class="search-box-wrapper">
                        <mdicon name="magnify" size="18" class="search-box-icon"></mdicon>
                        <input type="text" v-model="searchQuery" placeholder="Buscar ejercicio por nombre..."
                            class="search-box-input">
                    </div>

                    <div class="table-scroll-container">
                        <table class="exercise-selection-table">
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>NOMBRE</th>
                                    <th>SERIES</th>
                                    <th>REPS</th>
                                    <th>PESO</th>
                                    <th class="text-center">ACCIÓN</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="exercise in filteredExercises" :key="exercise.id"
                                    :class="{ 'row-is-selected': new_inforoutine.exercise_id === exercise.id }">
                                    <td>{{ exercise.id }}</td>
                                    <td class="font-bold">{{ exercise.name }}</td>
                                    <td>{{ exercise.sets }}</td>
                                    <td>{{ exercise.reps }}</td>
                                    <td>{{ exercise.weights }}</td>
                                    <td class="text-center">
                                        <button type="button" class="action-select-btn" @click="selecExercise(exercise)"
                                            :class="{ 'action-btn-active': new_inforoutine.exercise_id === exercise.id }">
                                            {{ new_inforoutine.exercise_id === exercise.id ? 'Asignado' : 'Asignar' }}
                                        </button>
                                    </td>
                                </tr>
                                <tr v-if="filteredExercises.length === 0">
                                    <td colspan="6" class="table-empty-state">No se encontraron ejercicios</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

            </div>

            <div class="form-actions-footer">
                <button type="submit" class="main-submit-btn">
                    AGREGAR EJERCICIO A LA RUTINA
                </button>
            </div>

        </form>
    </div>
</template>

<style scoped>
/* Contenedor principal alineado con tu fondo */
.routine-manager-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2.5rem 0; /* Más espacio arriba y abajo */
  background-color: #0b132b;
  min-height: calc(100vh - 70px);
  font-family: system-ui, -apple-system, sans-serif;
}

/* Tarjeta fluida con más padding interno (pasó de 1.75rem a 2.5rem) */
.routine-form-card {
  position: relative;
  background-color: #1c2541;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  padding: 2.5rem; /* Mayor amplitud interna */
  width: 90%; 
  max-width: 650px; 
  margin: 0 auto; 
  border: 1px solid rgba(255, 255, 255, 0.05);
  box-sizing: border-box;
}

/* Título principal con más separación inferior */
.form-main-title {
  font-size: 1.75rem; /* Un poco más grande */
  font-weight: 700;
  color: #ffffff;
  text-align: center;
  margin-top: 0;
  margin-bottom: 2rem; /* Más separación */
}

/* Botón cerrar flotante */
.close-floating-btn {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  background: linear-gradient(135deg, #f857a6, #ff5858);
  border: none;
  border-radius: 6px;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: opacity 0.2s;
  color: #ffffff;
}
.close-floating-btn:hover {
  opacity: 0.9;
}

/* Selector de días con más aire */
.day-selector-group {
  margin-bottom: 1.75rem;
}
.group-label {
  display: block;
  font-size: 0.85rem;
  font-weight: 700;
  color: #9ca3af;
  margin-bottom: 0.6rem;
  letter-spacing: 0.05em;
}
.days-radio-container {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem; /* Más separación entre los botones de días */
}
.day-radio-label {
  cursor: pointer;
  flex: 1;
  min-width: 85px;
}
.day-radio-input {
  display: none;
}
.day-radio-btn {
  display: block;
  text-align: center;
  padding: 0.65rem 0.35rem; /* Más alto */
  background-color: #0b132b;
  border: 1px solid #243056;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  color: #9ca3af;
  transition: all 0.15s ease;
}
.day-radio-input:checked + .day-radio-btn {
  background-color: #10b981;
  border-color: #10b981;
  color: #0b132b;
  font-weight: 700;
}

/* Contenedor vertical con mayor separación entre bloques */
.split-layout-container {
  display: flex;
  flex-direction: column;
  gap: 1.75rem; /* Más espacio entre el input de sección y la tabla */
}

.exercise-selector-panel {
  display: flex;
  flex-direction: column;
}

/* Campos de entrada con más altura interna (padding) */
.form-field-group {
  margin-bottom: 1.5rem;
}
.form-field-group label {
  display: block;
  font-size: 0.85rem;
  font-weight: 700;
  color: #9ca3af;
  margin-bottom: 0.6rem;
  letter-spacing: 0.05em;
}
.form-field-group input {
  width: 100%;
  padding: 0.75rem 1rem; /* Más cómodo para escribir, igual que tu captura */
  background-color: #0b132b;
  border: 1px solid #243056;
  border-radius: 6px;
  font-size: 1rem;
  color: #ffffff;
  box-sizing: border-box;
  transition: border-color 0.2s;
}
.form-field-group input:focus, .search-box-input:focus {
  outline: none;
  border-color: #10b981;
}

/* Subtítulo de asignación */
.panel-subtitle {
  font-size: 1.15rem;
  font-weight: 600;
  color: #ffffff;
  margin-top: 0;
  margin-bottom: 1rem;
}

/* Caja de búsqueda más alta */
.search-box-wrapper {
  position: relative;
  margin-bottom: 1rem;
}
.search-box-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #4b5563;
}
.search-box-input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 2.5rem;
  background-color: #0b132b;
  border: 1px solid #243056;
  border-radius: 6px;
  font-size: 0.95rem;
  color: #ffffff;
  box-sizing: border-box;
}

/* Tabla menos comprimida */
.table-scroll-container {
  border: 1px solid #243056;
  border-radius: 6px;
  max-height: 260px; /* Le di un poco más de altura para ver más filas holgadamente */
  overflow-y: auto;
  overflow-x: auto;
  background-color: #0b132b;
}

.exercise-selection-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  min-width: 480px;
}
.exercise-selection-table th {
  background-color: #161f38;
  padding: 0.8rem 1rem; /* Más espacio en el encabezado */
  color: #9ca3af;
  font-weight: 600;
  border-bottom: 1px solid #243056;
  position: sticky;
  top: 0;
  z-index: 10;
}
.exercise-selection-table td {
  padding: 0.75rem 1rem; /* Filas notablemente más altas y limpias */
  border-bottom: 1px solid #1c2541;
  color: #e5e7eb;
}

.font-bold { font-weight: 600; color: #ffffff; }
.text-center { text-align: center; }

/* Selección y acciones */
.row-is-selected {
  background-color: rgba(16, 185, 129, 0.08) !important;
}

.action-select-btn {
  background-color: #1c2541;
  border: 1px solid #3a4b7c;
  color: #9ca3af;
  padding: 0.4rem 1rem;
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s;
}
.action-select-btn:hover {
  background-color: #243056;
  color: #ffffff;
}
.action-btn-active {
  background-color: #10b981 !important;
  border-color: #10b981 !important;
  color: #0b132b !important;
  font-weight: 600;
}

.table-empty-state {
  text-align: center;
  color: #4b5563;
  padding: 2rem !important;
}

/* Botón de envío inferior amplio */
.form-actions-footer {
  margin-top: 2rem;
}
.main-submit-btn {
  width: 100%;
  background-color: #10b981;
  color: #0b132b;
  border: none;
  padding: 1rem; /* Botón idéntico en tamaño al verde de tu imagen */
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  cursor: pointer;
  transition: background-color 0.2s;
}
.main-submit-btn:hover {
  background-color: #059669;
}
</style>