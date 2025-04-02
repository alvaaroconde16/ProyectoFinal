<template>
  <header class="px-10 py-5 bg-gray-700 flex justify-between items-center text-white">
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
        <button @click="isLoginModalOpen = true" class="bg-blue-500 px-4 py-2 rounded hover:bg-blue-700">
          Iniciar Sesión
        </button>
      </template>
    </nav>
  </header>

  <!-- Modales -->
  <Login 
    :isModalOpen="isLoginModalOpen" 
    @closeModal="isLoginModalOpen = false" 
    @loginSuccess="handleLoginSuccess"
    @openRegisterModal="openRegisterFromLogin"
  />
  
  <Register 
    :isModalOpen="isRegisterModalOpen" 
    @closeModal="isRegisterModalOpen = false" 
    @registerSuccess="handleRegisterSuccess"
  />
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { getUser, logout } from '@/services/axios';
  import Login from '../registration/Login.vue';
  import Register from '../registration/Register.vue';
  import Logo from './Logo.vue';

  const user = ref(null);
  const isLoginModalOpen = ref(false);
  const isRegisterModalOpen = ref(false);
  const router = useRouter();

  const checkAuth = () => {
    user.value = getUser();
  };

  onMounted(() => {
    checkAuth();
  });

  const handleLogout = () => {
    logout();
    user.value = null;
    router.push('/');
  };

  const handleLoginSuccess = () => {
    checkAuth();
  };

  // Cerrar modal de login y abrir modal de registro
  const openRegisterFromLogin = () => {
    isLoginModalOpen.value = false;
    setTimeout(() => {
      isRegisterModalOpen.value = true;
    }, 300); // Pequeño delay para evitar conflictos visuales
  };

  const handleRegisterSuccess = () => {
    isRegisterModalOpen.value = false;
    setTimeout(() => {
      isLoginModalOpen.value = true;
    }, 300); // Pequeño delay para mejorar la experiencia
  };
</script>
