<script setup>
import { useAuthStore } from "../storage/auth";
import { useRouter } from "vue-router";
import { storeToRefs } from "pinia";
import { computed } from "vue";
import { useInfoUserStore } from "../storage/infousers";


const authStore = useAuthStore();
const { authenticated, auth_user } = storeToRefs(authStore);
const infouserStore = useInfoUserStore()

const props = defineProps({
  links: {
    type: Array,
    required: true,
  },
  rol_user: {
    type: String,
    required: true,
  },
});
const router = useRouter();
function closeSession() {
  authStore.logout();
  infouserStore.logout();
  router.push({ name: "Login" });
}

function myAccout(){

  router.push({name: "MyAccount"});
}
</script>
<template>
  <nav>
    <div class="nav-spacer" v-if="authenticated"></div>

    <ul>
      <li v-for="(link, index) in links" :key="index">
        <router-link v-if="!link.meta.rol_access && !authenticated" :to="link.path">{{ link.name }}
        </router-link>
      </li>

      <li v-for="(link, index) in links" :key="index">
        <router-link v-if="
          link.meta.rol_access &&
          authenticated &&
          link.meta.rol_access.includes(rol_user)
        " :to="link.path">{{ link.name }}
        </router-link>
      </li>
    </ul>
    
    <template v-if="authenticated">
      <div class="nav-user-section">
        <div class="user-profile-btn" @click="myAccout" title="Ver mi perfil">
          <mdicon name="account-circle" class="user-icon" /> 
          <span class="user-name">{{ auth_user }}</span>
        </div>
        
        <button @click="closeSession" class="logout-btn" title="Cerrar sesión">
          <mdicon name="logout" />
        </button>
      </div>
    </template>
  </nav>
</template>

<style scoped>
nav {
  background-color: #1c2541;
  color: #f1f5f9;            
  display: flex;
  justify-content: flex-start; /* Alinea todo al inicio (izquierda) */
  align-items: center;
  padding: 0 2rem;
  height: 75px;
  border-bottom: 1px solid #243056;
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.3);
  font-family: system-ui, -apple-system, sans-serif;
  position: relative; /* Mantiene la sección de usuario fija a la derecha */
  width: 100%;
  box-sizing: border-box;
}

ul {
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
  list-style: none;
  gap: 12px;
  margin-left: 4rem; /* El "empujón" hacia la derecha para que quede semi-centrado */
}

ul li a {
  color: #9ca3af !important;
  border-radius: 8px;
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 600;
  padding: 10px 20px;
  display: inline-block;
  letter-spacing: 0.03em;
  transition: all 0.2s ease-in-out;
}

ul li a:hover {
  background-color: #243056;
  color: #ffffff !important;
}

.router-link-active {
  background-color: rgba(16, 185, 129, 0.12) !important;
  color: #10b981 !important;                     
  font-weight: 700;
  border: 1px solid rgba(16, 185, 129, 0.2);
  box-shadow: 0 0 15px rgba(16, 185, 129, 0.1);
}

/* La sección de usuario se queda fija a la derecha sin afectar la posición de la lista */
.nav-user-section {
  position: absolute;
  right: 2rem;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  align-items: center;
  gap: 16px;
}

.user-profile-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: 30px;
  cursor: pointer;
  background-color: #0b132b;
  border: 1px solid #243056;
  transition: all 0.2s ease;
}

.user-profile-btn:hover {
  background: #243056;
  border-color: #3a4b7c;
  transform: translateY(-1px);
}

.user-icon {
  color: #10b981;
  display: flex;
  align-items: center;
}

.user-name {
  color: #ffffff;
  font-size: 0.9rem;
  font-weight: 600;
}

.logout-btn {
  background-color: transparent;
  border: none;
  color: #64748b;
  cursor: pointer;
  padding: 10px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.logout-btn:hover {
  background: rgba(239, 68, 68, 0.12);
  color: #ef4444;
  transform: scale(1.08);
}
</style>