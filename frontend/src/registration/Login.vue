<template>
  <div v-if="isModalOpen" class="fixed inset-0 flex items-center justify-center bg-black/50 z-50">
    <div class="bg-white p-8 rounded-lg shadow-lg w-96 relative">
      <!-- Botón de cierre -->
      <button @click="emit('closeModal')" class="absolute top-2 right-3 text-gray-600 text-2xl hover:text-gray-800 transition-colors">
        &times;
      </button>

      <!-- Título -->
      <h2 class="text-3xl font-semibold mb-3 text-center text-gray-900">Inicia Sesión</h2>
      <p class="text-sm text-gray-500 mb-8 text-center">Inicia sesión para reservas y gestionar tus citas</p>

      <!-- Formulario -->
      <form @submit.prevent="handleLogin">
        <!-- Campos de Entrada -->
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

        <!-- Botón de Iniciar Sesión -->
        <button type="submit" class="w-full bg-[#218cac] text-white py-3 rounded-lg hover:bg-[#1c7a8f] transition-colors focus:outline-none focus:ring-2 focus:ring-[#218cac] focus:ring-opacity-50">
          Iniciar Sesión
        </button>

        <!-- Link para Registrarse -->
        <p class="text-sm text-gray-600 mt-4 text-center">
          ¿No tienes cuenta? 
          <button @click="emit('openRegisterModal')" class="text-blue-500 hover:underline">
            Regístrate
          </button>
        </p>

        <!-- Mensaje de Error -->
        <p v-if="error" class="text-red-500 mt-4 text-center font-medium">{{ error }}</p>
      </form>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { login } from '@/services/axios';

  const router = useRouter();
  const username = ref('');
  const password = ref('');
  const error = ref('');

  const props = defineProps({
    isModalOpen: Boolean, // Estado del modal
  });
  const emit = defineEmits(['closeModal', 'loginSuccess', 'openRegisterModal']); // Nuevo evento para abrir el modal de registro

  const fields = ref([
    { id: 'username', label: 'Usuario', model: username, type: 'text' },
    { id: 'password', label: 'Contraseña', model: password, type: 'password' },
  ]);

  const handleLogin = async () => {
    error.value = ''; // Limpiar errores previos
    try {
      await login(username.value, password.value);

      emit('loginSuccess'); // Notificar al padre que el usuario inició sesión
      emit('closeModal'); // Cerrar el modal
    } catch (err) {
      error.value = 'Credenciales incorrectas';
    }
  };
</script>
