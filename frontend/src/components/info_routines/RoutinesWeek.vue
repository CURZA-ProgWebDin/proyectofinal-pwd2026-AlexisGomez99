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
    console.log("Creando rutina...")
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
                <button @click="addInfoRoutine" class="btn-primary">
                    Añadir Ejercicio
                </button>
                <button type="button" @click="router.back()" class="volver-btn" title="Volver">
                    <mdicon name="arrow-left" size="18"></mdicon>
                </button>
            </div>
        </div>

        <div v-else class="routine-content">
            <div class="routine-header-actions">
                <span class="routine-subtitle">Planificación semanal</span>
                <button @click="addInfoRoutine" class="btn-primary-sm">
                    <mdicon name="plus" size="16"></mdicon>
                    Agregar Ejercicio
                </button>
                <button type="button" @click="router.back()" class="volver-btn" title="Volver">
                    <mdicon name="arrow-left" size="18"></mdicon>
                </button>
            </div>

            <div v-for="(sections, day) in groupedRoutine" :key="day" class="day-card">
                <div class="day-header">
                    <mdicon name="calendar-range" size="22" class="day-icon"></mdicon>
                    <h2>{{ day }}</h2>
                </div>

                <div class="day-body">
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
    background-color: #0f172a;
    min-height: 100vh;
    padding: 40px 20px;
    box-sizing: border-box;
    font-family: 'Segoe UI', sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.loading-state {
    color: #f8fafc;
    text-align: center;
    padding: 60px;
    font-size: 18px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
}

.spinner {
    width: 40px;
    height: 40px;
    border: 4px solid rgba(16, 185, 129, 0.1);
    border-top-color: #10b981;
    border-radius: 50%;
    animation: spin 1s infinite linear;
}

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}

.empty-routine-card {
    background: #1e293b;
    border: 1px dashed #475569;
    border-radius: 12px;
    padding: 40px 20px;
    text-align: center;
    max-width: 500px;
    width: 100%;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.empty-state-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
}

.empty-icon {
    color: #64748b;
}

.empty-routine-card h3 {
    color: #f8fafc;
    margin: 0;
    font-size: 20px;
}

.empty-routine-card p {
    color: #94a3b8;
    font-size: 14px;
    margin: 0 0 10px 0;
    line-height: 1.5;
}

/* --- CONTENEDOR DE ACCIONES DE CABECERA --- */
.routine-header-actions {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-bottom: -10px;
}

.routine-subtitle {
    color: #94a3b8;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

/* --- BOTONES PRINCIPALES --- */
.btn-primary {
    background-color: #10b981;
    color: #0f172a;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    font-weight: 700;
    cursor: pointer;
    transition: background-color 0.2s;
}

.btn-primary:hover {
    background-color: #059669;
}

.btn-primary-sm {
    background-color: #10b981;
    color: #0f172a;
    border: none;
    padding: 8px 16px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 13px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s ease;
    box-shadow: 0 4px 10px rgba(16, 185, 129, 0.15);
}

.btn-primary-sm:hover {
    background-color: #059669;
    transform: translateY(-1px);
}

.btn-primary-sm:active {
    transform: translateY(0);
}

.routine-content {
    width: 100%;
    max-width: 950px;
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.day-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
    overflow: hidden;
}

.day-header {
    background: #111827;
    padding: 15px 25px;
    border-bottom: 1px solid #334155;
    display: flex;
    align-items: center;
    gap: 10px;
}

.day-icon {
    color: #10b981;
}

.day-header h2 {
    margin: 0;
    color: #f8fafc;
    font-size: 18px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.day-body {
    padding: 25px;
    display: flex;
    flex-direction: column;
    gap: 25px;
}

.section-group {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.section-title {
    margin: 0;
    color: #10b981;
    font-size: 14px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-left: 3px solid #10b981;
    padding-left: 8px;
}

.table-wrapper {
    border: 1px solid #334155;
    border-radius: 8px;
    overflow: hidden;
    background-color: #0f172a;
}

.exercises-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    text-align: left;
}

.exercises-table th,
.exercises-table td {
    padding: 14px 18px;
    color: #cbd5e1;
    vertical-align: middle;
}

.exercises-table th {
    background-color: #111827;
    color: #94a3b8;
    font-weight: 700;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 1px solid #334155;
}

.sub-th {
    text-transform: lowercase;
    font-size: 10px;
    color: #64748b;
    font-weight: normal;
}

.exercises-table tr:not(:last-child) td {
    border-bottom: 1px solid #1e293b;
}

.exercise-name {
    font-weight: 600;
    color: #f8fafc;
    width: 32%;
}

.recommended-cell {
    width: 22%;
}

.highlight-rec {
    color: #38bdf8;
    font-weight: 700;
}

.weight-rec {
    color: #94a3b8;
    font-size: 13px;
    margin-left: 4px;
}

.real-data-badge {
    background-color: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.2);
    color: #34d399;
    padding: 6px 12px;
    border-radius: 20px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 13px;
}

.real-data-badge strong {
    color: #f8fafc;
}

.success-icon {
    color: #10b981;
}

.no-data-text {
    color: #64748b;
    font-size: 13px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-style: italic;
}

.pencil-icon {
    color: #475569;
}

.text-center {
    text-align: center;
}

.video-link {
    color: #ef4444;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    transition: color 0.2s, transform 0.1s;
}

.video-link:hover {
    color: #f87171;
    transform: scale(1.15);
}

.no-video {
    color: #334155;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    cursor: not-allowed;
}

/* --- ESTILOS DE LA COLUMNA ACCIONES --- */
.actions-header {
    text-align: center;
    width: 12%;
    /* Ajustado el ancho para que quepan holgadamente dos botones */
}

.actions-cell {
    text-align: center;
}

.actions-wrapper {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    /* Espacio entre el botón de editar y eliminar */
}

/* Estilo Base de Botones de Icono */
.btn-icon-edit,
.btn-icon-delete {
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 6px;
    border-radius: 6px;
    transition: background-color 0.2s, transform 0.1s, color 0.2s;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

/* Botón Editar (Verde) */
.btn-icon-edit {
    color: #10b981;
}

.btn-icon-edit:hover {
    background-color: rgba(16, 185, 129, 0.15);
    transform: scale(1.05);
}

.btn-icon-edit:active {
    transform: scale(0.95);
}

/* Botón Eliminar (Rojo destructivo) */
.btn-icon-delete {
    color: #64748b;
    /* Gris apagado por defecto para que no grite 'atención' innecesariamente */
}

.btn-icon-delete:hover {
    color: #f87171;
    /* Rojo brillante al hacer hover */
    background-color: rgba(239, 68, 68, 0.15);
    transform: scale(1.05);
}

.btn-icon-delete:active {
    transform: scale(0.95);
}

/* Responsividad */
@media (max-width: 600px) {
    .routine-header-actions {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
        margin-bottom: 5px;
    }

    .btn-primary-sm {
        width: 100%;
        justify-content: center;
    }
}
.volver-btn {
    top: 16px;
    right: 16px;
    width: 32px;
    height: 32px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background-color: #ef4444;
    color: #f8fafc;
    box-shadow: 0 4px 10px rgba(239, 68, 68, 0.25);
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    font-weight: 700;
    cursor: pointer;
    transition: background-color 0.2s;
}

.volver-btn:hover {
    background-color: #dc2626;
}

.volver-btn:active {
    transform: scale(0.92);
}
</style>