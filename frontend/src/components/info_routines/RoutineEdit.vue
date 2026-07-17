<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter, useRoute } from "vue-router";
import { storeToRefs } from "pinia";
import { useInfoRoutineStore } from "../../storage/inforoutines";

const router = useRouter();
const route = useRoute();
const infoRoutineStore = useInfoRoutineStore();
const { infoRoutineEdit } = storeToRefs(infoRoutineStore);
const { update, getOne } = infoRoutineStore;

const loading = ref(true);

onMounted(async () => {
    try {
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


async function editar() {
    await update(infoRoutineEdit.value);
    router.back();
}
</script>

<template>
    <div class="edit-routine-page">
        <div v-if="loading" class="loading-state">
            <div class="spinner"></div>
            <p>Cargando datos...</p>
        </div>

        <div v-else class="flex-layout">
            <div class="form-column">
                <div class="form-card">
                    <form @submit.prevent="editar" class="custom-form">
                        <button type="button" @click="router.back()" class="cancel-btn" title="Cancelar">
                            <mdicon name="close" size="18"></mdicon>
                        </button>

                        <h2>Editar Ejercicio de Rutina</h2>

                        <div class="form-grid">
                            
                            <div class="left-pane">
                                <div class="form-group">
                                    <label>SERIES</label>
                                    <input type="text" v-model="infoRoutineEdit.sets" placeholder="Ej: 4">
                                </div>
                                <div class="form-group">
                                    <label>REPETICIONES</label>
                                    <input type="text" v-model="infoRoutineEdit.reps" placeholder="Ej: 12">
                                </div>
                                <div class="form-group">
                                    <label>PESO</label>
                                    <input type="text" v-model="infoRoutineEdit.weights" placeholder="Ej: 20kg">
                                </div>
                            </div>

                            <div class="right-pane">
                                <div class="form-group flex-grow">
                                    <label>COMENTARIO DEL EJERCICIO</label>
                                    <textarea 
                                        v-model="infoRoutineEdit.comment" 
                                        placeholder="Agrega anotaciones sobre la técnica o sensaciones de este ejercicio..."
                                        rows="4"
                                    ></textarea>
                                </div>
                                <div class="form-group flex-grow">
                                    <label>DESCRIPCIÓN</label>
                                    <textarea 
                                        v-model="infoRoutineEdit.description" 
                                        placeholder="Instrucciones o detalles de ejecución..."
                                        rows="4"
                                    ></textarea>
                                </div>
                            </div>

                        </div>

                        <button type="submit" class="submit-btn">
                            ACEPTAR CAMBIOS
                        </button>
                    </form>
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
    max-width: 900px; /* Reducido para que el formulario se sienta compacto y elegante */
    width: 100%;
    margin: 0 auto;
}

.form-column {
    flex: 1;
    width: 100%;
    display: flex;
    flex-direction: column;
}

.form-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    padding: 35px;
    width: 100%;
    box-sizing: border-box;
}

.custom-form {
    position: relative;
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 25px;
}

h2 {
    margin-top: 0;
    margin-bottom: 5px;
    color: #f8fafc;
    text-align: left;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

/* --- DISEÑO DE GRILLA (2 COLUMNAS) --- */
.form-grid {
    display: grid;
    grid-template-columns: 1fr 1.5fr; /* 1 parte a la izquierda, 1.5 partes a la derecha */
    gap: 30px;
    width: 100%;
}

.left-pane {
    display: flex;
    flex-direction: column;
    gap: 18px;
}

.right-pane {
    display: flex;
    flex-direction: column;
    gap: 18px;
}

.form-group {
    display: flex;
    flex-direction: column;
}

.form-group.flex-grow {
    flex-grow: 1;
}

label {
    font-size: 11px;
    font-weight: 800;
    margin-bottom: 8px;
    color: #94a3b8;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* --- ESTILOS DE ENTRADA (INPUTS & TEXTAREAS) --- */
input[type="text"],
textarea {
    padding: 12px 14px;
    border: 1px solid #475569;
    border-radius: 8px;
    font-size: 14px;
    color: #f8fafc;
    background-color: #0f172a;
    transition: all 0.2s ease;
    outline: none;
    width: 100%;
    box-sizing: border-box;
}

textarea {
    resize: none; /* Desactiva el redimensionado manual feo */
    line-height: 1.5;
    font-family: inherit;
}

input[type="text"]:focus,
textarea:focus {
    border-color: #10b981;
    box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.15);
    background-color: #0b1120;
}

/* Spinner de carga */
.loading-state {
    color: #f8fafc;
    text-align: center;
    padding: 40px;
    font-size: 18px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
}

.spinner {
    width: 35px;
    height: 35px;
    border: 3px solid rgba(16, 185, 129, 0.1);
    border-top-color: #10b981;
    border-radius: 50%;
    animation: spin 1s infinite linear;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

/* --- BOTÓN DE ENVIAR --- */
.submit-btn {
    width: 100%;
    padding: 14px;
    background-color: #10b981;
    color: #0f172a;
    border: none;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.5px;
    cursor: pointer;
    transition: background-color 0.2s ease, transform 0.1s ease;
    margin-top: 15px;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2);
}

.submit-btn:hover {
    background-color: #059669;
}

.submit-btn:active {
    transform: scale(0.99);
}

/* --- BOTÓN CANCELAR --- */
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
    background-color: #334155; /* Estilo más sobrio, grisáceo, para no distraer tanto */
    color: #94a3b8;
    border: 1px solid #475569;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s ease;
    z-index: 10;
}

.cancel-btn:hover {
    background-color: #ef4444; /* Pasa a rojo destructivo solo al hacer hover */
    color: #f8fafc;
    border-color: #ef4444;
    box-shadow: 0 4px 10px rgba(239, 68, 68, 0.25);
}

.cancel-btn:active {
    transform: scale(0.92);
}

/* --- RESPONSIVIDAD --- */
@media (max-width: 768px) {
    .form-grid {
        grid-template-columns: 1fr; /* Pasa a una sola columna en móviles */
        gap: 18px;
    }

    .form-card {
        padding: 25px;
    }

    .cancel-btn {
        top: -5px;
        right: -5px;
    }
}
</style>