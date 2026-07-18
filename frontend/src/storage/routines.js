import { ref } from "vue";
import ApiService from "../service/ApiService";
import { defineStore } from "pinia";
import { reactive } from "vue";

export const useRoutineStore = defineStore("routines", () => {
  const routine = ref({});
  const routines = ref([]);
  const loading = ref(false);
  const api_service = new ApiService("/routines/");
  const routineEdit = reactive({
    id: '',
    name: '',
    user: '',
    user_id: ''
  });

  async function listRoutines() {
    loading.value = true;
    const data = await api_service.getAll();
    if (data) {
      routines.value = data;
    }
    loading.value = false;
  }

  async function getOne(id) {
    loading.value = true;
    const data = await api_service.findOne(id);
    if (data) {
      routine.value = data;
      routineEdit.id = data.id;
      routineEdit.name = data.name;
      routineEdit.user = data.user?.name;
      routineEdit.user_id = data.user_id;
    }
    loading.value = false;
  }

  async function create(data) {
    await api_service.create(data);
  }

  async function update(data) {
    await api_service.update(data, data.id);
  }
  async function getRoutinesFrom(id) {
    await api_service.getRoutinesFrom(id);
    if (data) {
      routines.value = data;
    }
    loading.value = false;
  }
  async function destroy(id) {
    await api_service.destroy(id);
  }
  function setRoutine(routine) {
    routineEdit.id = routine.id;
    routineEdit.name = routine.name;
    routineEdit.user = routine.user;
    routineEdit.user_id = routine.user_id;
  }
  return { routines, routine, routineEdit, create, destroy, update, getOne, listRoutines, setRoutine,getRoutinesFrom };
});