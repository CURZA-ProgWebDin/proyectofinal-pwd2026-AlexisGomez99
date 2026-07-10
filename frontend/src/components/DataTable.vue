<script setup>
import { computed } from "vue";
const props = defineProps({
  headers: {
    type: Array,
    required: true,
  },
  data: {
    type: Array,
    required: true,
  },
  acciones: {
    type: Boolean,
    default: true,
  },
});

const emits = defineEmits(["editar", "eliminar"]);
const items = computed(() => {
  if (props.data.length === 0) {
    return [];
  }
  const values = props.data.map((item) => {
    const row = [];
    for (const key in item) {
      if (props.headers.includes(key.toUpperCase())) {
        row[props.headers.indexOf(key.toUpperCase())] = item[key];
      }
    }
    return row;
  });
  return values;
});

function eliminar(value) {
  const item = props.data.find((i) => {
    for (const key in i) {
      if (props.headers.includes(key.toUpperCase()) && i[key] === value[0]) {
        return true;
      }
    }
  });

  emits("eliminar", item);
}
function editar(value) {
  const item = props.data.find((i) => {
    for (const key in i) {
      if (props.headers.includes(key.toUpperCase()) && i[key] === value[0]) {
        return true;
      }
    }
  });
  emits("editar", item);
}
</script>
<template>
  <section class="table-wrapper">
    <div v-if="items.length === 0" class="no-records">
      <h2>Registros no encontrados</h2>
    </div>
    
    <table v-else class="modern-table">
      <thead>
        <tr>
          <th v-for="head in headers" :key="head">{{ head }}</th>
          <th v-if="acciones" class="text-center">ACCIONES</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in items" :key="index">
          <td v-for="(cell, indexCell) in row" :key="indexCell">{{ cell }}</td>
          <td v-if="acciones" class="actions-cell">
            <button class="btn btn-edit" @click="editar(row)" title="Editar">
              <mdicon name="pencil" size="18"></mdicon>
            </button>
            <button class="btn btn-danger" @click="eliminar(row)" title="Eliminar">
              <mdicon name="trash-can" size="18"></mdicon>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<style scoped>
.table-wrapper {
  width: 100%;
  overflow-x: auto;
  background-color: #1e293b;
}

.no-records {
  text-align: center;
  padding: 2rem;
  color: #94a3b8;
}

.no-records h2 {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 500;
  letter-spacing: 0.5px;
}

.modern-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.9rem;
  background-color: #1e293b;
}

th {
  background-color: #0f172a; 
  color: #94a3b8; 
  padding: 12px 16px;
  font-weight: 700;
  font-size: 0.8rem;
  letter-spacing: 1px;
  border-bottom: 2px solid #334155;
  text-transform: uppercase;
}

td {
  padding: 12px 16px;
  border-bottom: 1px solid #334155;
  color: #e2e8f0;
  vertical-align: middle;
}

tr:hover td {
  background-color: #243249; 
  transition: background-color 0.15s ease;
}

.text-center {
  text-align: center;
}

.actions-cell {
  text-align: center;
  white-space: nowrap; 
  width: 100px; 
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: none;
  cursor: pointer;
  padding: 6px; 
  border-radius: 4px;
  margin: 0 4px;
  transition: background-color 0.2s ease, transform 0.1s ease;
  color: #ffffff;
}

.btn-edit {
  background-color: #10b981;
  color: #0f172a;
}

.btn-edit:hover {
  background-color: #059669;
}

.btn-danger {
  background-color: #ef4444;
}

.btn-danger:hover {
  background-color: #dc2626;
}

.btn:active {
  transform: scale(0.92);
}
</style>