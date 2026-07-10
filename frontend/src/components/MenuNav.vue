<script setup>
import { useAuthStore } from "../storage/auth";
import { useRouter } from "vue-router";
import { storeToRefs } from "pinia";
import { computed } from "vue";
const authStore = useAuthStore();
const { authenticated, auth_user } = storeToRefs(authStore);

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
function cerrarSesion() {
  authStore.logout();
  router.push({ name: "Login" });
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
      <p>
        <mdicon name="account-circle" /> {{ auth_user }}
      </p>
      <button @click="cerrarSesion">
        <mdicon name="logout" />
      </button>
    </template>
  </nav>
</template>

<style scoped>
nav {
  background-color: #0f172a; 
  color: #f8fafc;            
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 10px 30px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

ul {
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
  list-style: none;
  gap: 5px; 
  flex-grow: 1;
}

ul li {
  margin: 0;
}

ul li a {
  color: #38bdf8 !important; 
  border-radius: 5px;
  text-decoration: none;
  font-size: 1rem;
  font-weight: 500;
  padding: 8px 16px;
  display: inline-block;
  transition: all 0.2s ease;
}

ul li a:hover {
  background-color: #334155; /* Gris azulado al pasar el mouse */
  color: #ffffff !important;
}

/* Clase activa de Vue Router */
.router-link-active {
  background-color: #1e293b !important; /* Fondo azul intermedio para la solapa activa */
  color: #ffffff !important;             /* Texto full blanco para resaltar */
  font-weight: 600;
}

button {
  background-color: transparent;
  border: none;
  color: #fff;
  cursor: pointer;
}
</style>