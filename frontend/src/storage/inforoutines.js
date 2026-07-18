import { ref } from "vue";
import ApiService from "../service/ApiService";
import { defineStore } from "pinia";
import { reactive } from "vue";

export const useInfoRoutineStore = defineStore("inforoutines", () => {
  const inforoutine = ref({});
  const inforoutines = ref([]);
  const loading = ref(false);
  const api_service = new ApiService("/info_routines/");
  const infoRoutineEdit = reactive({
    id: '',
    day: '',
    comment: '',
    description: '',
    sets: '',
    reps: '',
    weights: '',
    name_section: '',
    exercise_id: '',
    routine_id: '',
  });

  async function listInfoRoutines() {
    loading.value = true;
    const data = await api_service.getAll();
    if (data) {
      inforoutines.value = data;
    }
    loading.value = false;
  }

  async function getOne(id) {
    loading.value = true;
    const data = await api_service.findOne(id);
    if (data) {
      inforoutine.value = data;
      infoRoutineEdit.id = data.id;
      infoRoutineEdit.day = data.day;
      infoRoutineEdit.name_section = data.name_section;
      infoRoutineEdit.exercise_id = data.exercise_id;
      infoRoutineEdit.comment = data.comment;
      infoRoutineEdit.description = data.description;
      infoRoutineEdit.reps = data.reps;
      infoRoutineEdit.sets = data.sets;
      infoRoutineEdit.weights = data.weights;
      infoRoutineEdit.routine_id = data.routine_id;
    }
    loading.value = false;
  }
  async function getRoutine(id) {
    loading.value = true;
    const data = await api_service.getRoutine(id);
    if (data) {
      inforoutines.value = data;
      infoRoutineEdit.id = data.id;
      infoRoutineEdit.day = data.day;
      infoRoutineEdit.name_section = data.name_section;
      infoRoutineEdit.exercise_id = data.exercise_id;
      infoRoutineEdit.comment = data.comment;
      infoRoutineEdit.description = data.description;
      infoRoutineEdit.reps = data.reps;
      infoRoutineEdit.sets = data.sets;
      infoRoutineEdit.weights = data.weights;
      infoRoutineEdit.routine_id = data.routine_id;
    }
    loading.value = false;
  }

  async function create(data) {
    await api_service.create(data);
  }

  async function update(data) {
    await api_service.update(data, data.id);
  }

  async function destroy(id) {
    await api_service.destroy(id);
  }
  function logout() {
    inforoutine.value = {}
  }
  function setInfoRoutine(inforoutine) {
    infoRoutineEdit.id = inforoutine.id;
    infoRoutineEdit.day = inforoutine.day;
    infoRoutineEdit.name_section = inforoutine.name_section;
    infoRoutineEdit.exercise_id = inforoutine.exercise_id;
    infoRoutineEdit.comment = inforoutine.comment;
    infoRoutineEdit.description = inforoutine.description;
    infoRoutineEdit.reps = inforoutine.reps;
    infoRoutineEdit.sets = inforoutine.sets;
    infoRoutineEdit.weights = inforoutine.weights;
    infoRoutineEdit.routine_id = inforoutine.routine_id;

  }
  return { inforoutines, inforoutine, infoRoutineEdit, create, destroy, update, getOne, logout, listInfoRoutines, setInfoRoutine, getRoutine };
});