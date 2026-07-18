import { ref } from "vue";
import ApiService from "../service/ApiService";
import { defineStore } from "pinia";
import { reactive } from "vue";

export const useUserStore = defineStore("users", () => {
  const user = ref({});
  const users = ref([]);
  const loading = ref(false);
  const api_service = new ApiService("/users/");
  const userEdit = reactive({
    id: '',
    name: '',
    email: '',
    rol_id: '',
    rol: ''
  });

  async function listUsers() {
    loading.value = true;
    const data = await api_service.getAll();
    if (data) {
      users.value = data;
    }
    loading.value = false;
  }

  async function getOne(id) {
    loading.value = true;
    const data = await api_service.findOne(id);
    if (data) {
      user.value = data;
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
  function setUser(user) {
    userEdit.id = user.id;
    userEdit.name = user.name;
    userEdit.email = user.email;
    userEdit.rol = user.rol;
    userEdit.rol_id = user.rol_id
  }
  return { users, user, userEdit, create, destroy,update, getOne, listUsers, setUser };
});