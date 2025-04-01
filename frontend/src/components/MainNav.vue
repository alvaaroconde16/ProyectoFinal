<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Link from './Link.vue';
import Logo from './Logo.vue';

const user = ref(null);
const router = useRouter();

// Verificar si el usuario está logueado
const checkAuth = () => {
  const storedUser = localStorage.getItem('user');
  if (storedUser) {
    user.value = JSON.parse(storedUser);
  }
};

// Se ejecuta cuando el componente se monta
onMounted(() => {
  checkAuth();
});

// Cerrar sesión
const logout = () => {
  localStorage.removeItem('user');
  localStorage.removeItem('token');
  user.value = null;
  router.push('/'); // Redirigir al Home
};
</script>

<template>
  <header class="px-10 py-5 bg-gray-700 flex justify-between items-center absolute top-0 w-full z-10 text-white">
    <div>
      <Logo />
    </div>

    <nav class="flex items-center gap-4">
      <Link to="home">Inicio</Link>

      <template v-if="user">
        <span class="text-sm font-semibold">Hola, {{ user.username }}</span>
        <button @click="logout" class="bg-red-500 px-3 py-1 rounded hover:bg-red-700">
          Cerrar Sesión
        </button>
      </template>

      <template v-else>
        <button @click="router.push('/login')" class="bg-green-500 px-3 py-1 rounded hover:bg-green-700">
          Iniciar Sesión
        </button>
      </template>
    </nav>
  </header>
</template>
