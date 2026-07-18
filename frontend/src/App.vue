<script setup>
import { useRoute } from 'vue-router';
import MenuNav from './components/MenuNav.vue';
import { useAuthStore } from './storage/auth.js';
import { routes } from './routes/configs/navigation.js'
import { storeToRefs } from 'pinia';
import ToadComponent from "./components/ToadComponent.vue";

const authStore = useAuthStore();
const { rol_user, authenticated } = storeToRefs(authStore);
const route = useRoute();
</script>

<template>
  <toad-component />
  <div id="app">
    <header>
      <MenuNav :links="routes" :rol_user="rol_user" :authenticated="authenticated" />
    </header>

    <main>
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
  </div>
</template>

<style>
html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  box-sizing: border-box;
  color: white;
  background-color: #0f172a;
}
</style>