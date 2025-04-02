<template>
    <div v-if="isModalOpen" class="fixed inset-0 flex items-center justify-center bg-black/50 z-50">
      <div class="bg-white p-8 rounded-lg shadow-lg w-96 relative">
        <button @click="emit('closeModal')" class="absolute top-2 right-3 text-gray-600 text-2xl hover:text-gray-800 transition-colors">
          &times;
        </button>
        <h2 class="text-2xl font-semibold mb-6 text-center text-gray-900">Crear una cuenta</h2>
        <p>Rellena tus datos para empezar a usar BeautyLink</p>
  
        <form @submit.prevent="handleRegister">
          <div class="mb-6">
            <label class="block text-gray-700 font-medium">Nombre de Usuario</label>
            <input v-model="username" type="text" class="w-full px-4 py-3 mt-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500" required />
          </div>
  
          <div class="mb-6">
            <label class="block text-gray-700 font-medium">Correo Electrónico</label>
            <input v-model="email" type="email" class="w-full px-4 py-3 mt-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500" required />
          </div>
  
          <div class="mb-6">
            <label class="block text-gray-700 font-medium">Contraseña</label>
            <input v-model="password" type="password" class="w-full px-4 py-3 mt-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500" required />
          </div>
  
          <button type="submit" class="w-full bg-[#218cac] text-white py-3 rounded-lg hover:bg-[#1c7a8f] transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">
            Registrarse
          </button>
  
          <p class="text-sm text-gray-600 mt-4 text-center">
            ¿Ya tienes cuenta? <router-link to="/login" class="text-blue-500 hover:underline">Inicia sesión</router-link>
          </p>
  
          <p v-if="error" class="text-red-500 mt-4 text-center font-medium">{{ error }}</p>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
    import { ref, defineProps, defineEmits } from 'vue';
    import { useRouter } from 'vue-router';
    import { register } from '@/services/axios';
  
    const router = useRouter();
    const username = ref('');
    const email = ref('');
    const password = ref('');
    const error = ref('');
  
    const props = defineProps({
      isModalOpen: Boolean, // Estado del modal
    });
    const emit = defineEmits(['closeModal', 'registerSuccess']); // Emitimos eventos al padre
  
    const handleRegister = async () => {
      error.value = ''; // Limpiar errores previos
      try {
        // Llamada a la API para registrar el usuario
        await register(username.value, email.value, password.value);
  
        emit('registerSuccess'); // Notificar al padre que el usuario se registró
        emit('closeModal'); // Cerrar el modal
      } catch (err) {
        error.value = 'Hubo un problema al registrarse. Intenta de nuevo.';
      }
    };
  </script>
  