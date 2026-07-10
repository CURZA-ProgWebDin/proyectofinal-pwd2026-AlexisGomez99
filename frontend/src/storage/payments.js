import { ref } from "vue";
import ApiService from "../service/ApiService";
import { defineStore } from "pinia";
import { reactive } from "vue";

export const usePaymentStore = defineStore("payments", () => {
  const payment = ref({});
  const payments = ref([]);
  const loading = ref(false);
  const api_service = new ApiService("/payments/");
  const paymentEdit = reactive({
    id: '',
    amount: '',
    description: '',
    service: '',
    user_id: '',
    user: ''
  });

  async function listPayments() {
    loading.value = true;
    const data = await api_service.getAll();
    if (data) {
      payments.value = data;
    }
    loading.value = false;
  }

  async function getOne(id) {
    loading.value = true;
    const data = await api_service.findOne(id);
    if (data) {
      payment.value = data;
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
  function setPayment(payment) {
    paymentEdit.id = payment.id;
    paymentEdit.amount = payment.amount;
    paymentEdit.description = payment.description;
    paymentEdit.service = payment.service;
    paymentEdit.user_id = payment.user_id
    paymentEdit.user = payment.user
  }
  return { payments, payment, paymentEdit, create, destroy,update, getOne, listPayments, setPayment };
});