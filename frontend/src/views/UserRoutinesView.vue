<script setup>
import { useRoute } from 'vue-router';
import RoutinesList from '../components/routines/RoutinesList.vue'; 

const route = useRoute();

</script>

<template>
  <div >
    <RoutinesList :user_id="route.query.user_id" />
  </div>
</template>