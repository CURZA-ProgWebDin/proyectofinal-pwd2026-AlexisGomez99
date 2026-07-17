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
  background-color: #1e2530; 
  color: #f1f5f9;            
  display: flex;
  justify-content: space-between; 
  align-items: center;
  padding: 0 32px;
  height: 70px;
  border-bottom: 1px solid #2d3748;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  font-family: 'Segoe UI', system-ui, sans-serif;
}

ul {
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
  list-style: none;
  gap: 8px; 
}

ul li a {
  color: #94a3b8 !important;
  border-radius: 8px;
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 500;
  padding: 8px 16px;
  display: inline-block;
  transition: all 0.25s ease;
}

ul li a:hover {
  background-color: #252f3f;
  color: #f1f5f9 !important;
}

.router-link-active {
  background-color: rgba(59, 130, 246, 0.1) !important;
  color: #3b82f6 !important;                            
  font-weight: 600;
}

.nav-user-section {
  display: flex;
  align-items: center;
  gap: 16px;
}

.user-profile-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  border-radius: 30px;
  cursor: pointer;
  border: 1px solid transparent;
  transition: all 0.2s ease;
}

.user-profile-btn:hover {
  background: #252f3f;
  border-color: #2d3748;
}

.user-icon {
  color: #3b82f6;
  display: flex;
  align-items: center;
}

.user-name {
  color: #f1f5f9;
  font-size: 0.95rem;
  font-weight: 500;
}

.logout-btn {
  background-color: transparent;
  border: none;
  color: #64748b;
  cursor: pointer;
  padding: 8px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.logout-btn:hover {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  transform: scale(1.05);
}
</style>