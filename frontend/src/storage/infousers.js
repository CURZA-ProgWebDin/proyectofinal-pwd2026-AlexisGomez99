import { ref } from "vue";
import ApiService from "../service/ApiService";
import { defineStore } from "pinia";
import { reactive } from "vue";

export const useInfoUserStore = defineStore("infousers", () => {
  const infouser = ref({});
  const infousers = ref([]);
  const loading = ref(false);
  const api_service = new ApiService("/info_users/");
  const infoUserEdit = reactive({
    id: '',
    dni: '',
    name: '',
    last_name: '',
    number_phone: '',
    adress: ''
  });

  async function listInfoUsers() {
    loading.value = true;
    const data = await api_service.getAll();
    if (data) {
      infousers.value = data;
    }
    loading.value = false;
  }

  async function getOne(id) {
    loading.value = true;
    const data = await api_service.findOne(id);
    if (data) {
      infouser.value = data;
    }
    loading.value = false;
  }
  async function getMe() {
    loading.value = true;
    const data = await api_service.getMe();
    if (data) {
      infouser.value = data;
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
    infouser.value = {}
  }
  function setInfoUser(user) {
    infoUserEdit.id = user.id;
    infoUserEdit.name = user.name;
    infoUserEdit.last_name = user.last_name;
    infoUserEdit.dni = user.dni;
    infoUserEdit.number_phone = user.number_phone,
    infoUserEdit.adress = user.adress
  }
  return { infousers, infouser, infoUserEdit, create, destroy, update, getOne, logout, listInfoUsers, setInfoUser,getMe };
});