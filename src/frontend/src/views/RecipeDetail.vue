<template>
  <div>
    <div v-if="loading" class="text-center py-8">
      <p class="text-gray-500">Loading recipe...</p>
    </div>
    
    <div v-else-if="error" class="bg-red-50 p-4 rounded-md text-red-700 mb-6">
      {{ error }}
    </div>
    
    <div v-else class="bg-white rounded-lg shadow-md p-6">
      <div class="flex justify-between items-start mb-4">
        <h2 class="text-2xl font-bold">{{ recipe.name }}</h2>
        <span 
          v-if="!recipe.is_public" 
          class="px-2 py-1 text-xs bg-gray-200 text-gray-700 rounded-full"
        >
          Private
        </span>
      </div>
      
      <p class="text-gray-600 mb-6">{{ recipe.description_short }}</p>
      
      <div class="prose max-w-none" v-html="renderedMarkdown"></div>
      
      <div class="mt-8 text-sm text-gray-500">
        <p>Created: {{ formatDate(recipe.created_at) }}</p>
        <p>Last updated: {{ formatDate(recipe.updated_at) }}</p>
      </div>
      
      <div class="mt-6 flex space-x-4">
        <router-link to="/" class="px-4 py-2 bg-gray-200 text-gray-700 rounded-md hover:bg-gray-300">
          Back to Recipes
        </router-link>
        
        <template v-if="recipe.creator === 'user@example.com'">
          <router-link 
            :to="`/edit/${recipe.id}`" 
            class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
          >
            Edit Recipe
          </router-link>
          
          <button 
            @click="deleteRecipe" 
            class="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700"
          >
            Delete Recipe
          </button>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, inject, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { marked } from 'marked';
import { recipeService } from '../services/recipeService';

const route = useRoute();
const router = useRouter();

const recipe = ref({});
const loading = ref(true);
const error = ref(null);

const renderedMarkdown = computed(() => {
  if (!recipe.value.description_md) return '';
  return marked(recipe.value.description_md);
});

onMounted(async () => {
  try {
    const id = parseInt(route.params.id);
    recipe.value = await recipeService.getRecipe(id);
  } catch (err) {
    error.value = err.message || 'Failed to load recipe';
  } finally {
    loading.value = false;
  }
});

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString();
};

const deleteRecipe = async () => {
  if (!confirm('Are you sure you want to delete this recipe?')) {
    return;
  }
  
  try {
    loading.value = true;
    await recipeService.deleteRecipe(recipe.value.id);
    router.push('/');
  } catch (err) {
    error.value = err.message || 'Failed to delete recipe';
  } finally {
    loading.value = false;
  }
};
</script>

<style>
/* Add some basic styling for markdown content */
.prose {
  line-height: 1.6;
}

.prose h1 {
  font-size: 1.8rem;
  font-weight: bold;
  margin-top: 1.5rem;
  margin-bottom: 1rem;
}

.prose h2 {
  font-size: 1.5rem;
  font-weight: bold;
  margin-top: 1.5rem;
  margin-bottom: 0.75rem;
}

.prose ul, .prose ol {
  padding-left: 1.5rem;
  margin-bottom: 1rem;
}

.prose ul {
  list-style-type: disc;
}

.prose ol {
  list-style-type: decimal;
}

.prose p {
  margin-bottom: 1rem;
}
</style>