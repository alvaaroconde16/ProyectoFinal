<template>
  <header class="px-10 py-5 bg-gray-700 flex justify-between items-center absolute top-0 w-full z-10 text-white">
    <div>
      <Logo />
    </div>

    <nav class="flex items-center gap-4">
      <template v-if="user">
        <span class="text-sm font-semibold">Hola, {{ user.username }}</span>
        <button @click="handleLogout" class="bg-red-500 px-3 py-1 rounded hover:bg-red-700">
          Cerrar Sesión
        </button>
      </template>

      <template v-else>
        <button @click="isModalOpen = true" class="bg-blue-500 px-4 py-2 rounded hover:bg-blue-700">
          Iniciar Sesión
        </button>
      </template>
    </nav>
  </header>

  <!-- Modal de Login -->
  <Login :isModalOpen="isModalOpen" @closeModal="isModalOpen = false" @loginSuccess="handleLoginSuccess" />
</template>

<script>
import Login from '../registration/Login.vue';
export default {
  components: { Login },
};
</script>

<script setup>
  import { ref, onMounted, defineEmits } from 'vue';
  import { useRouter } from 'vue-router';
  import { getUser, logout, register } from '@/services/axios';
  import Logo from './Logo.vue';

  const user = ref(null);
  const isModalOpen = ref(false);
  const router = useRouter();
  const emit = defineEmits(['openLoginModal']); // Emitimos evento para abrir el modal

  const checkAuth = () => {
    user.value = getUser();
  };

  // Se ejecuta cuando el componente se monta
  onMounted(() => {
    checkAuth();
  });

  // Manejo de cierre de sesión
  const handleLogout = () => {
    logout();
    user.value = null;
    router.push('/'); // Redirigir al Home
  };

  // Manejo de inicio de sesión
  const handleLoginSuccess = () => {
    checkAuth(); // Actualizar el usuario después del login
  };
</script>