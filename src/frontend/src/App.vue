<script setup>
import { provide } from 'vue';
import NavBar from "./components/NavBar.vue";
import Dialog from "./components/Dialog.vue";
import Loading from "./components/Loading.vue";
import { recipeService } from './services/recipeService';

</script>

<template>
  <div id="app">
    <NavBar />
    <router-view />
    <Loading />
    <Dialog />
  </div>
</template>

<script>
provide('recipeService', recipeService);
// Provide the recipe service to all components
// provide('recipeService', recipeService);
export default {
  name: 'App',
  components: {
    NavBar,
  },
}
</script>

<style>
@import 'https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css';
</style>
