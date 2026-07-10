import { ref } from "vue";
import ApiService from "../service/ApiService";
import { defineStore } from "pinia";
import { reactive } from "vue";

export const useExerciseStore = defineStore("exercises", () => {
  const exercise = ref({});
  const exercises = ref([]);
  const loading = ref(false);
  const api_service = new ApiService("/exercises/");
  const exerciseEdit = reactive({
    id: '',
    name: '',
    reps: '',
    sets: '',
    example_link: '',
    weights: ''
  });

  async function listExercises() {
    loading.value = true;
    const data = await api_service.getAll();
    if (data) {
      exercises.value = data;
    }
    loading.value = false;
  }

  async function getOne(id) {
    loading.value = true;
    const data = await api_service.findOne(id);
    if (data) {
      exercise.value = data;
    }
    loading.value = false;
  }

  async function create(data) {
    await api_service.create(data);
  }

  async function update(data) {
    await api_service.update(data,data.id);
  }

  async function destroy(id) {
    await api_service.destroy(id);
  }
  function setExercise(exercise) {
    exerciseEdit.id = exercise.id;
    exerciseEdit.name = exercise.name;
    exerciseEdit.reps = exercise.reps;
    exerciseEdit.sets = exercise.sets;
    exerciseEdit.weights = exercise.weights
    exerciseEdit.example_link = exercise.example_link
  }
  return { exercises, exercise, exerciseEdit,  create, destroy,update, getOne, listExercises, setExercise };
});