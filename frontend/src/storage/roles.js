import { ref } from "vue";
import ApiService from "../service/ApiService";
import { defineStore } from "pinia";
import { reactive } from "vue";

export const useRolesStore = defineStore("roles", () => {
  const rol = ref({});
  const roles = ref([]);
  const loading = ref(false);
  const api_service = new ApiService("/roles/");
  const rolEdit = reactive({
    id: '',
    name: '',
  });

  async function list() {
    loading.value = true;
    const data = await api_service.getAll();
    if (data) {
      roles.value = data;
    }
    loading.value = false;
  }

  async function getOne(id) {
    loading.value = true;
    const data = await api_service.findOne(id);
    if (data) {
      rol.value = data;
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
  function setRol(rol) {
    rolEdit.id = rol.id;
    rolEdit.name = rol.name;
  }
  return { roles, rol, rolEdit,  create, destroy,update, getOne, list, setRol };
});