<script setup>
import { onMounted, ref } from 'vue';
import { useAuthStore } from '../storage/auth';
import ExercisesList from './exercises/ExercisesList.vue';
import RoutinesList from './routines/RoutinesList.vue';

const authStore = useAuthStore();
const { auth_user, id, rol_user } = authStore

// Listado de frases y consejos de entrenamiento
const recomendaciones = [
    {
        icon: 'lightning-bolt',
        title: 'La clave es la constancia',
        desc: 'No busques entrenar perfecto hoy, busca entrenar siempre. Cada repetición suma al resultado final.'
    },
    {
        icon: 'scale-balance',
        title: 'Sobrecarga Progresiva',
        desc: 'Para que tu músculo crezca, intenta mejorar un poco en cada sesión: una repetición extra, mejor técnica o un poco más de peso.'
    },
    {
        icon: 'heart-pulse',
        title: 'Escucha a tu cuerpo',
        desc: 'El descanso y la nutrición son tan importantes como el entrenamiento. Si sientes dolor articular, baja la intensidad hoy.'
    },
    {
        icon: 'water',
        title: 'Mantente hidratado',
        desc: 'Perder solo un 2% de agua corporal puede reducir tu fuerza y rendimiento físico hasta un 15%. ¡Toma agua entre series!'
    }
];

const recomendacionDelDia = ref(recomendaciones[0]);

onMounted(() => {
    const randomIndex = Math.floor(Math.random() * recomendaciones.length);
    recomendacionDelDia.value = recomendaciones[randomIndex];
});
</script>

<template>
    <div class="home-container">
        <header class="welcome-header">
            <div class="header-content">
                <span class="welcome-label">¡Hola de nuevo!</span>
                <h1>Bienvenido, <span class="highlight-text">{{ auth_user }}</span></h1>
                <p class="role-badge">Rol: {{ rol_user }}</p>
            </div>
            
            <div class="tip-card">
                <div class="tip-header">
                    <div class="tip-icon-wrapper">
                        <mdicon :name="recomendacionDelDia.icon" size="20"></mdicon>
                    </div>
                    <h4>Consejo del Día</h4>
                </div>
                <h5>{{ recomendacionDelDia.title }}</h5>
                <p>{{ recomendacionDelDia.desc }}</p>
            </div>
        </header>

        <main class="home-content">
            <div v-if="rol_user === 'operador' || rol_user === 'creador'" class="routines-section">
                <div class="section-title-wrapper">
                    <mdicon name="dumbbell" size="22" class="title-icon"></mdicon>
                    <h3>Tus Rutinas Asignadas</h3>
                </div>
                <RoutinesList :user_id="id" />
            </div>
        </main>
    </div>
</template>

<style scoped>
.home-container {
    background-color: #0f172a;
    min-height: 100vh;
    padding: 40px 20px;
    box-sizing: border-box;
    font-family: 'Segoe UI', sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 30px;
}

/* --- CABECERA DE BIENVENIDA --- */
.welcome-header {
    width: 100%;
    max-width: 950px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    align-items: center;
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 35px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    box-sizing: border-box;
}

.header-content {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.welcome-label {
    color: #10b981;
    font-size: 13px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}

.welcome-header h1 {
    margin: 0;
    color: #f8fafc;
    font-size: 32px;
    font-weight: 800;
    line-height: 1.2;
}

.highlight-text {
    background: linear-gradient(to right, #10b981, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.role-badge {
    margin: 4px 0 0 0;
    color: #94a3b8;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    background-color: #1e293b;
    border: 1px solid #475569;
    padding: 4px 10px;
    border-radius: 20px;
    display: inline-block;
    align-self: flex-start;
}

/* --- TARJETA DE RECOMENDACIÓN --- */
.tip-card {
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    transition: transform 0.2s ease, border-color 0.2s;
}

.tip-card:hover {
    border-color: #10b981;
    transform: translateY(-2px);
}

.tip-header {
    display: flex;
    align-items: center;
    gap: 10px;
}

.tip-icon-wrapper {
    background-color: rgba(16, 185, 129, 0.1);
    color: #10b981;
    padding: 6px;
    border-radius: 8px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

.tip-header h4 {
    margin: 0;
    color: #10b981;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.tip-card h5 {
    margin: 0;
    color: #f8fafc;
    font-size: 15px;
    font-weight: 700;
}

.tip-card p {
    margin: 0;
    color: #94a3b8;
    font-size: 13px;
    line-height: 1.5;
}

/* --- SECCIÓN DE CONTENIDO --- */
.home-content {
    width: 100%;
    max-width: 950px;
}

.routines-section {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.section-title-wrapper {
    display: flex;
    align-items: center;
    gap: 10px;
    padding-bottom: 5px;
}

.title-icon {
    color: #10b981;
}

.section-title-wrapper h3 {
    margin: 0;
    color: #f8fafc;
    font-size: 18px;
    font-weight: 700;
}

/* --- RESPONSIVIDAD --- */
@media (max-width: 768px) {
    .welcome-header {
        grid-template-columns: 1fr;
        gap: 25px;
        padding: 25px;
    }

    .welcome-header h1 {
        font-size: 26px;
    }
}
</style>
