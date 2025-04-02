<template>
  <div v-if="isModalOpen" class="fixed inset-0 flex items-center justify-center bg-black/50 z-50">
    <div class="bg-white p-8 rounded-lg shadow-lg w-96 relative">
      <!-- Botón de cierre -->
      <button @click="emit('closeModal')" class="absolute top-2 right-3 text-gray-600 text-2xl hover:text-gray-800 transition-colors">
        &times;
      </button>

      <!-- Título -->
      <h2 class="text-3xl font-semibold mb-4 text-center text-gray-900">Regístrate</h2>
      <p class="text-sm text-gray-500 mb-10 text-center">Rellena tus datos para empezar a usar BeautyLink</p>

      <form @submit.prevent="handleRegister">
        <!-- Campos con Floating Labels -->
        <div v-for="(field, index) in fields" :key="index" class="relative mb-7">
          <input
            :id="field.id"
            v-model="field.model"
            :type="field.type"
            class="peer w-full border border-gray-300 rounded-lg px-4 pt-5 pb-2 focus:ring-2 focus:ring-[#218cac] focus:border-[#218cac] placeholder-transparent"
            placeholder=" "
            required
          />
          <label
            :for="field.id"
            class="absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-500 text-sm transition-all duration-300 ease-in-out peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-placeholder-shown:text-gray-400 peer-focus:top-3 peer-focus:text-xs peer-focus:text-[#218cac] peer-valid:top-3 peer-valid:text-xs peer-valid:text-gray"
          >
            {{ field.label }}
          </label>
        </div>

        <!-- Botón de Registro -->
        <button type="submit" class="w-full bg-[#218cac] text-white py-3 rounded-lg hover:bg-[#1c7a8f] transition-colors focus:outline-none focus:ring-2 focus:ring-[#218cac]">
          Registrarse
        </button>

        <!-- Mensaje de Error -->
        <p v-if="error" class="text-red-500 mt-4 text-center font-medium">{{ error }}</p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { register } from '@/services/axios';

const username = ref('');
const email = ref('');
const telefono = ref('');
const password = ref('');
const rol = ref('cliente');
const error = ref('');

const props = defineProps({ isModalOpen: Boolean });
const emit = defineEmits(['closeModal', 'registerSuccess']);

const fields = ref([
  { id: 'username', label: 'Usuario', model: username, type: 'text' },
  { id: 'email', label: 'Correo Electrónico', model: email, type: 'email' },
  { id: 'telefono', label: 'Teléfono', model: telefono, type: 'text' },
  { id: 'password', label: 'Contraseña', model: password, type: 'password' },
]);

const handleRegister = async () => {
  error.value = '';
  try {
    await register(username.value, email.value, telefono.value, password.value, rol.value);
    emit('registerSuccess');
    emit('closeModal');
  } catch (err) {
    error.value = 'Error al registrar el usuario';
  }
};
</script>
