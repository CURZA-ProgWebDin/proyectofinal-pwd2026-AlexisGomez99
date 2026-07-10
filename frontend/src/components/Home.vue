<script setup>
import { useAuthStore } from '../storage/auth';
import ExercisesList from './exercises/ExercisesList.vue';

const authStore = useAuthStore();
const {auth_user} = authStore

</script>

<template>
    <h1>Bienvenido {{ auth_user }}!</h1>
    
</template>

