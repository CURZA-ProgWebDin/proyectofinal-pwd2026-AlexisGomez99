<script setup>
import { useRoute, useRouter } from 'vue-router';
import { useInfoRoutineStore } from '../../storage/inforoutines';
import { useExerciseStore } from '../../storage/exercises';
import { onMounted, ref, computed } from 'vue';
import { storeToRefs } from 'pinia';

const router = useRouter();
const route = useRoute();

const infoRoutineStore = useInfoRoutineStore();
const exerciseStore = useExerciseStore();

const { inforoutines } = storeToRefs(infoRoutineStore);
const { exercises } = storeToRefs(exerciseStore);

const { getRoutine, setInfoRoutine } = infoRoutineStore;
const { listExercises } = exerciseStore;

const loading = ref(true);
const activeDay = ref(null);

const toggleDay = (day) => {
    activeDay.value = activeDay.value === day ? null : day;
}
onMounted(async () => {
    await Promise.all([
        getRoutine(route.params.id),
        listExercises()
    ]);
    loading.value = false;
});

const groupedRoutine = computed(() => {
    const groups = {};

    inforoutines.value.forEach((item) => {
        const day = item.day || 'SIN DÍA';
        const section = item.name_section || 'GENERAL';

        const matchedExercise = exercises.value.find(ex => ex.id === item.exercise_id);

        const enrichedItem = {
            ...item,
            exercise_name: matchedExercise ? matchedExercise.name : `Ejercicio #${item.exercise_id}`,
            exercise: matchedExercise,

            rec_sets: matchedExercise?.sets || '-',
            rec_reps: matchedExercise?.reps || '-',
            rec_weights: matchedExercise?.weights || '-',

            has_real_data: item.sets !== "" || item.reps !== "" || item.weights !== "",
            real_sets: item.sets,
            real_reps: item.reps,
            real_weights: item.weights
        };

        if (!groups[day]) {
            groups[day] = {};
        }
        if (!groups[day][section]) {
            groups[day][section] = [];
        }

        groups[day][section].push(enrichedItem);
    });

    return groups;
});

function addInfoRoutine() {
    router.push({ name: 'InfoRoutinesWeekCreate', params: { id: route.params.id } })
}

function editarInfoRoutine(exercise) {
    setInfoRoutine(exercise)
    router.push({ name: 'InfoRoutinesWeekEdit', params: { id: exercise.id } })
}

function deleteInfoRoutine(exercise) {
    console.log("Eliminando el registro de info_routine con ID:", exercise.id);
}
</script>

<template>
    <div class="routines-week-container">

        <div v-if="loading" class="loading-state">
            <div class="spinner"></div>
            <p>Cargando ejercicios...</p>
        </div>

        <div v-else-if="inforoutines.length === 0" class="empty-routine-card">
            <div class="empty-state-content">
                <mdicon name="dumbbell" size="48" class="empty-icon"></mdicon>
                <h3>Esta rutina no tiene ejercicios</h3>
                <p>Haz clic en el botón de abajo para empezar a añadir ejercicios a la rutina.</p>
                <div class="empty-actions">
                    <button type="button" @click="router.back()" class="volver-btn" title="Volver">
                        <mdicon name="arrow-left" size="18"></mdicon>
                        <span>Volver</span>
                    </button>
                    <button @click="addInfoRoutine" class="btn-primary">
                        Añadir Ejercicio
                    </button>
                </div>
            </div>
        </div>

        <div v-else class="routine-content">
            <div class="routine-header-actions">
                <div class="header-left">
                    <button type="button" @click="router.back()" class="volver-btn" title="Volver">
                        <mdicon name="arrow-left" size="18"></mdicon>
                    </button>
                    <span class="routine-subtitle">Planificación semanal</span>
                </div>
                <button @click="addInfoRoutine" class="btn-primary-sm">
                    <mdicon name="plus" size="16"></mdicon>
                    Agregar Ejercicio
                </button>
            </div>

            <div v-for="(sections, day) in groupedRoutine" :key="day" class="day-card" :class="{ 'day-card-active': activeDay === day }">
                <div class="day-header" @click="toggleDay(day)" role="button" :aria-expanded="activeDay === day">
                    <div class="day-header-left">
                        <mdicon name="calendar-range" size="22" class="day-icon"></mdicon>
                        <h2>{{ day }}</h2>
                    </div>
                    <div class="day-header-right">
                        <mdicon :name="activeDay === day ? 'chevron-up' : 'chevron-down'" size="24" class="arrow-icon"></mdicon>
                    </div>
                </div>

                <div v-show="activeDay === day" class="day-body">
                    <div v-for="(exercisesList, section) in sections" :key="section" class="section-group">
                        <h3 class="section-title">{{ section }}</h3>

                        <div class="table-wrapper">
                            <table class="exercises-table">
                                <thead>
                                    <tr>
                                        <th>EJERCICIO</th>
                                        <th>RECOMENDADO <span class="sub-th">(Series x Reps - Peso)</span></th>
                                        <th>MIS MARCAS / NOTAS</th>
                                        <th class="text-center">VIDEO</th>
                                        <th class="actions-header">ACCIONES</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="exercise in exercisesList" :key="exercise.id">
                                        <td class="exercise-name">
                                            {{ exercise.exercise_name }}
                                        </td>
                                        <td class="recommended-cell">
                                            <span class="highlight-rec">
                                                {{ exercise.rec_sets }}x{{ exercise.rec_reps }}
                                            </span>
                                            <span class="weight-rec" v-if="exercise.rec_weights !== '-'">
                                                ({{ exercise.rec_weights }})
                                            </span>
                                        </td>
                                        <td>
                                            <div v-if="exercise.has_real_data" class="real-data-badge">
                                                <mdicon name="check-circle" size="14" class="success-icon"></mdicon>
                                                <span>
                                                    Realizado: <strong>{{ exercise.real_sets || 0 }}x{{
                                                        exercise.real_reps || 0 }}</strong>
                                                    <span v-if="exercise.real_weights"> @ {{ exercise.real_weights
                                                    }}</span>
                                                </span>
                                            </div>
                                            <span v-else class="no-data-text">
                                                <mdicon name="pencil-outline" size="14" class="pencil-icon"></mdicon>
                                                Sin registrar hoy
                                            </span>
                                        </td>
                                        <td class="text-center">
                                            <a v-if="exercise.exercise?.example_link"
                                                :href="exercise.exercise.example_link" target="_blank"
                                                rel="noopener noreferrer" class="video-link"
                                                title="Ver video explicativo">
                                                <mdicon name="play-circle" size="22"></mdicon>
                                            </a>
                                            <span v-else class="no-video" title="No hay video disponible">
                                                <mdicon name="play-circle-outline" size="22"></mdicon>
                                            </span>
                                        </td>
                                        <td class="actions-cell">
                                            <div class="actions-wrapper">
                                                <button @click="editarInfoRoutine(exercise)" class="btn-icon-edit"
                                                    title="Editar">
                                                    <mdicon name="pencil" size="18"></mdicon>
                                                </button>
                                                <button @click="deleteInfoRoutine(exercise)" class="btn-icon-delete"
                                                    title="Eliminar">
                                                    <mdicon name="trash-can" size="18"></mdicon>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<style scoped>
.routines-week-container {
  width: 90%;
  max-width: 1000px;
  margin: 2rem auto;
  font-family: system-ui, -apple-system, sans-serif;
  box-sizing: border-box;
}

.routine-header-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  gap: 1rem;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.routine-subtitle {
  font-size: 1.5rem;
  font-weight: 700;
  color: #ffffff;
}

.volver-btn {
  background-color: #1c2541;
  border: 1px solid #243056;
  color: #9ca3af;
  width: 40px;
  height: 40px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
}
.volver-btn:hover {
  background-color: #243056;
  color: #ffffff;
  border-color: #3a4b7c;
}

.btn-primary-sm {
  background-color: #10b981;
  color: #0b132b;
  border: none;
  padding: 0.65rem 1.2rem;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: background-color 0.2s;
}
.btn-primary-sm:hover {
  background-color: #059669;
}

.day-card {
  background-color: #1c2541;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  margin-bottom: 1rem;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  transition: border-color 0.2s, box-shadow 0.2s;
}
.day-card-active {
  border-color: rgba(16, 185, 129, 0.3);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
}

.day-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.25rem 1.75rem;
  background-color: #161f38;
  cursor: pointer;
  user-select: none;
  transition: background-color 0.2s;
}
.day-header:hover {
  background-color: #1e294b;
}

.day-header-left {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.day-header-left h2 {
  font-size: 1.15rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0;
  letter-spacing: 0.03em;
}
.day-icon {
  color: #10b981;
}
.arrow-icon {
  color: #6b7280;
  transition: color 0.2s;
}
.day-header:hover .arrow-icon {
  color: #ffffff;
}

.day-body {
  padding: 1.75rem;
  background-color: #1c2541;
  display: flex;
  flex-direction: column;
  gap: 1.75rem;
}

.section-group {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.section-title {
  font-size: 1rem;
  font-weight: 600;
  color: #9ca3af;
  margin: 0;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.table-wrapper {
  border: 1px solid #243056;
  border-radius: 8px;
  overflow-x: auto;
  background-color: #0b132b;
}
.exercises-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  min-width: 700px;
}
.exercises-table th {
  background-color: #0f172a;
  padding: 1rem;
  color: #9ca3af;
  font-weight: 600;
  text-align: left;
  border-bottom: 1px solid #243056;
}
.sub-th {
  font-size: 0.75rem;
  color: #6b7280;
  font-weight: 400;
}
.exercises-table td {
  padding: 1rem;
  border-bottom: 1px solid #1c2541;
  color: #e5e7eb;
  vertical-align: middle;
}

.exercise-name {
  font-weight: 600;
  color: #ffffff;
}
.highlight-rec {
  color: #10b981;
  font-weight: 600;
}
.weight-rec {
  color: #9ca3af;
  margin-left: 0.25rem;
}

.real-data-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  background-color: rgba(16, 185, 129, 0.1);
  padding: 0.4rem 0.75rem;
  border-radius: 6px;
  color: #10b981;
  font-size: 0.85rem;
}
.no-data-text {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  color: #6b7280;
  font-size: 0.85rem;
}

.video-link {
  color: #3b82f6;
  display: inline-block;
  transition: transform 0.15s;
}
.video-link:hover {
  transform: scale(1.1);
  color: #60a5fa;
}
.no-video {
  color: #374151;
}

.actions-header { text-align: center !important; }
.actions-cell { width: 100px; }
.actions-wrapper {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
}
.btn-icon-edit, .btn-icon-delete {
  background: none;
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color 0.2s;
}
.btn-icon-edit { color: #f59e0b; }
.btn-icon-edit:hover { background-color: rgba(245, 158, 11, 0.1); }
.btn-icon-delete { color: #ef4444; }
.btn-icon-delete:hover { background-color: rgba(239, 68, 68, 0.1); }

.loading-state, .empty-routine-card {
  background-color: #1c2541;
  border-radius: 12px;
  padding: 4rem 2rem;
  text-align: center;
  border: 1px solid rgba(255, 255, 255, 0.05);
}
.spinner {
  border: 3px solid #243056;
  border-top: 3px solid #10b981;
  border-radius: 50%;
  width: 35px;
  height: 35px;
  margin: 0 auto 1rem;
  animation: spin 1s linear infinite;
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.empty-state-content h3 { font-size: 1.3rem; color: #ffffff; margin: 1rem 0 0.5rem; }
.empty-state-content p { color: #9ca3af; margin-bottom: 2rem; font-size: 0.95rem; }
.empty-icon { color: #4b5563; }
.empty-actions {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}
.btn-primary {
  background-color: #10b981;
  color: #0b132b;
  border: none;
  padding: 0.75rem 1.75rem;
  border-radius: 8px;
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
}
.empty-actions .volver-btn {
  flex-direction: row;
  width: auto;
  padding: 0 1.2rem;
  gap: 0.5rem;
  font-size: 0.9rem;
  font-weight: 600;
}
</style>