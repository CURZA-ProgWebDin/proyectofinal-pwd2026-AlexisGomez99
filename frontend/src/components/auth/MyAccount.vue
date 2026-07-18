<script setup>
import { onMounted, onUnmounted, ref } from 'vue';
import { storeToRefs } from 'pinia';
import { useInfoUserStore } from '../../storage/infousers.js';
import { useAuthStore } from '../../storage/auth.js';
import InfoUsersCreate from './InfoUsersCreate.vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const infouserStore = useInfoUserStore();
const authStore = useAuthStore();

const { id, auth_user } = storeToRefs(authStore);
const { infouser } = storeToRefs(infouserStore);
const { getMe, setInfoUser } = infouserStore;

const loading = ref(true);
const info = ref(false);

onMounted(async () => {
    await getMe();
    if (infouser.value && Object.keys(infouser.value).length > 0) {
        info.value = true;
    }

    loading.value = false;
});
onUnmounted(()=> {
    info.value = false;
})

function editAccount() {
    setInfoUser(infouser.value);
    router.push({ name: 'InfoUsersEdit' });
}
</script>

<template>
    <div class="profile-container">
        <div v-if="loading" class="loading-state">
            <p>Cargando perfil...</p>
        </div>

        <div v-else>
            <div v-if="!info">
                <InfoUsersCreate></InfoUsersCreate>
            </div>

            <div v-else class="profile-card">
                <div class="profile-header">
                    <div class="avatar-placeholder">
                        {{ infouser.name?.charAt(0).toUpperCase() }}{{ infouser.last_name?.charAt(0).toUpperCase() }}
                    </div>
                    <div class="profile-title">
                        <h2>{{ infouser.name }} {{ infouser.last_name }}</h2>
                        <span class="role-badge">{{auth_user}}</span>
                    </div>
                    <button type="button" @click="editAccount" class="edit-btn" title="Editar cuenta">
                        <mdicon name="pencil" size="18"></mdicon>
                    </button>
                </div>

                <div class="profile-body">
                    <div class="info-block">
                        <div class="info-label-group">
                            <mdicon name="card-account-details-outline" class="info-icon" size="20"></mdicon>
                            <span>Documento Nacional de Identidad</span>
                        </div>
                        <p class="info-value">{{ infouser.dni }}</p>
                    </div>

                    <div class="info-block">
                        <div class="info-label-group">
                            <mdicon name="phone-outline" class="info-icon" size="20"></mdicon>
                            <span>Teléfono de Contacto</span>
                        </div>
                        <p class="info-value">{{ infouser.number_phone || 'No especificado' }}</p>
                    </div>

                    <div class="info-block">
                        <div class="info-label-group">
                            <mdicon name="home-map-marker" class="info-icon" size="20"></mdicon>
                            <span>Dirección de Residencia</span>
                        </div>
                        <p class="info-value">{{ infouser.adress || 'No especificada' }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.profile-container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2.5rem;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}

.loading-state {
    color: #64748b;
    font-size: 1.1rem;
}

.profile-card {
    background: #1e2530;
    border-radius: 16px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4), 0 5px 15px rgba(0, 0, 0, 0.2);
    width: 100%;
    max-width: 540px;
    overflow: hidden;
    border: 1px solid #2d3748;
}

.profile-header {
    display: flex;
    align-items: center;
    gap: 18px;
    background: linear-gradient(180deg, #252f3f 0%, #1e2530 100%);
    padding: 30px 28px 22px 28px;
    border-bottom: 1px solid #2d3748;
}

.avatar-placeholder {
    width: 68px;
    height: 68px;
    background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
    color: #ffffff;
    font-size: 1.4rem;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3);
}

.profile-title {
    flex-grow: 1;
}

.profile-title h2 {
    margin: 0;
    font-size: 1.45rem;
    color: #f8fafc;
    font-weight: 600;
    letter-spacing: -0.3px;
}

.role-badge {
    display: inline-block;
    background-color: rgba(37, 99, 235, 0.15);
    color: #60a5fa;
    font-size: 0.75rem;
    padding: 3px 10px;
    border-radius: 9999px;
    margin-top: 6px;
    font-weight: 500;
    border: 1px solid rgba(37, 99, 235, 0.2);
}

.edit-btn {
    background: #252f3f;
    border: 1px solid #374151;
    color: #9ca3af;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
}

.edit-btn:hover {
    background: #374151;
    color: #f9fafb;
    transform: scale(1.05);
}

.profile-body {
    padding: 16px 28px 32px 28px;
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.info-block {
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding-bottom: 16px;
    border-bottom: 1px solid #2d3748;
}

.info-block:last-child {
    border-bottom: none;
    padding-bottom: 0;
}

.info-label-group {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #94a3b8;
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.info-icon {
    color: #64748b;
    display: flex;
    align-items: center;
}

.info-value {
    margin: 0;
    padding-left: 30px;
    font-size: 1.1rem;
    color: #f1f5f9;
    font-weight: 500;
    word-break: break-word;
}
</style>