import { createApp } from 'vue';
import App from './App.vue';
import { createPinia } from 'pinia';
import { router } from './routes';
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import mdiVue from 'mdi-vue/v3'
import * as mdijs from "@mdi/js";

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);
const app = createApp(App);
app.use(mdiVue, { icons: mdijs });
app.use(router);
app.use(pinia);
app.mount('#app');