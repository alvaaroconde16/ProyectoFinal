<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const username = ref('');
const password = ref('');
const error = ref('');

const login = async () => {
  error.value = ''; // Limpiar errores previos
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/token/', {
      username: username.value,
      password: password.value,
    });

    // Guardar el token y el usuario en localStorage
    localStorage.setItem('token', response.data.access);
    localStorage.setItem('user', JSON.stringify({ username: username.value }));

    router.push('/'); // Redirigir al home
  } catch (err) {
    error.value = 'Credenciales incorrectas';
  }
};
</script>

<template>
  <div class="flex justify-center items-center h-screen bg-gray-100">
    <div class="bg-white p-8 rounded shadow-lg w-96">
      <h2 class="text-2xl font-bold mb-4 text-center">Iniciar Sesión</h2>

      <form @submit.prevent="login">
        <div class="mb-4">
          <label class="block text-gray-700">Usuario</label>
          <input v-model="username" type="text" class="w-full px-3 py-2 border rounded" required />
        </div>

        <div class="mb-4">
          <label class="block text-gray-700">Contraseña</label>
          <input v-model="password" type="password" class="w-full px-3 py-2 border rounded" required />
        </div>

        <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-700">
          Iniciar Sesión
        </button>

        <p v-if="error" class="text-red-500 mt-2 text-center">{{ error }}</p>
      </form>
    </div>
  </div>
</template>
