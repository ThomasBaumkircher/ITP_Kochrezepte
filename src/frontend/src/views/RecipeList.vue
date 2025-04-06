<template>
  <div>
    <h2 class="text-2xl font-bold mb-6">All Recipes</h2>
    
    <div v-if="loading" class="text-center py-8">
      <p class="text-gray-500">Loading recipes...</p>
    </div>
    
    <div v-else-if="error" class="bg-red-50 p-4 rounded-md text-red-700 mb-6">
      {{ error }}
    </div>
    
    <div v-else-if="recipes.length === 0" class="text-center py-8">
      <p class="text-gray-500">No recipes found. Create your first recipe!</p>
      <router-link to="/create" class="mt-4 inline-block px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700">
        Create Recipe
      </router-link>
    </div>
    
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div 
        v-for="recipe in recipes" 
        :key="recipe.id" 
        class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow"
      >
        <div class="p-6">
          <div class="flex justify-between items-start">
            <h3 class="text-xl font-semibold text-gray-900">{{ recipe.name }}</h3>
            <span 
              v-if="!recipe.is_public" 
              class="px-2 py-1 text-xs bg-gray-200 text-gray-700 rounded-full"
            >
              Private
            </span>
          </div>
          <p class="mt-2 text-gray-600">{{ recipe.description_short }}</p>
          <div class="mt-4 flex justify-between items-center">
            <router-link 
              :to="`/recipe/${recipe.id}`" 
              class="text-green-600 hover:text-green-800"
            >
              View Recipe
            </router-link>
            <div v-if="recipe.creator === 'user@example.com'" class="flex space-x-2">
              <router-link 
                :to="`/edit/${recipe.id}`" 
                class="text-blue-600 hover:text-blue-800"
              >
                Edit
              </router-link>
              <button 
                @click="deleteRecipe(recipe.id)" 
                class="text-red-600 hover:text-red-800"
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, inject, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { recipeService } from '../services/recipeService';

const router = useRouter();

const recipes = ref([]);
const loading = ref(true);
const error = ref(null);

onMounted(async () => {
  try {
    recipes.value = await recipeService.getAllRecipes();
  } catch (err) {
    error.value = err.message || 'Failed to load recipes';
  } finally {
    loading.value = false;
  }
});

const deleteRecipe = async (id) => {
  if (!confirm('Are you sure you want to delete this recipe?')) {
    return;
  }
  
  try {
    loading.value = true;
    await recipeService.deleteRecipe(id);
    recipes.value = recipes.value.filter(recipe => recipe.id !== id);
  } catch (err) {
    error.value = err.message || 'Failed to delete recipe';
  } finally {
    loading.value = false;
  }
};
</script>