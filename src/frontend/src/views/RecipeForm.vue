<template>
  <div>
    <h2 class="text-2xl font-bold mb-6">{{ isEditing ? 'Edit Recipe' : 'Create Recipe' }}</h2>
    
    <div v-if="loading" class="text-center py-8">
      <p class="text-gray-500">Loading...</p>
    </div>
    
    <div v-else-if="error" class="bg-red-50 p-4 rounded-md text-red-700 mb-6">
      {{ error }}
    </div>
    
    <form v-else @submit.prevent="submitForm" class="bg-white rounded-lg shadow-md p-6">
      <div class="mb-4">
        <label for="name" class="block text-sm font-medium text-gray-700 mb-1">Recipe Name</label>
        <input
          id="name"
          v-model="form.name"
          type="text"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
        />
      </div>
      
      <div class="mb-4">
        <label for="description_short" class="block text-sm font-medium text-gray-700 mb-1">Short Description</label>
        <input
          id="description_short"
          v-model="form.description_short"
          type="text"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
        />
      </div>
      
      <div class="mb-4">
        <label for="description_md" class="block text-sm font-medium text-gray-700 mb-1">
          Full Recipe (Markdown)
          <span class="text-xs text-gray-500 ml-1">Use Markdown for formatting</span>
        </label>
        <textarea
          id="description_md"
          v-model="form.description_md"
          rows="10"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
        ></textarea>
      </div>
      
      <div class="mb-6">
        <div class="flex items-center">
          <input
            id="is_public"
            v-model="form.is_public"
            type="checkbox"
            class="h-4 w-4 text-green-600 focus:ring-green-500 border-gray-300 rounded"
          />
          <label for="is_public" class="ml-2 block text-sm text-gray-700">
            Make this recipe public
          </label>
        </div>
      </div>
      
      <div class="flex justify-between">
        <router-link 
          to="/" 
          class="px-4 py-2 bg-gray-200 text-gray-700 rounded-md hover:bg-gray-300"
        >
          Cancel
        </router-link>
        <button 
          type="submit" 
          class="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700"
          :disabled="submitting"
        >
          {{ submitting ? 'Saving...' : (isEditing ? 'Update Recipe' : 'Create Recipe') }}
        </button>
      </div>
    </form>
    
    <div v-if="showPreview" class="mt-8">
      <h3 class="text-xl font-bold mb-4">Preview</h3>
      <div class="bg-white rounded-lg shadow-md p-6">
        <h2 class="text-2xl font-bold mb-2">{{ form.name }}</h2>
        <p class="text-gray-600 mb-6">{{ form.description_short }}</p>
        <div class="prose max-w-none" v-html="renderedMarkdown"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, inject, computed, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { marked } from 'marked';
import { recipeService } from '../services/recipeService';

const route = useRoute();
const router = useRouter();

const form = ref({
  name: '',
  description_short: '',
  description_md: '',
  is_public: false
});

const loading = ref(false);
const submitting = ref(false);
const error = ref(null);
const showPreview = ref(false);

const isEditing = computed(() => route.name === 'edit-recipe');

const renderedMarkdown = computed(() => {
  if (!form.value.description_md) return '';
  return marked(form.value.description_md);
});

onMounted(async () => {
  if (isEditing.value) {
    try {
      loading.value = true;
      const id = parseInt(route.params.id);
      const recipe = await recipeService.getRecipe(id);
      
      form.value = {
        name: recipe.name,
        description_short: recipe.description_short,
        description_md: recipe.description_md,
        is_public: recipe.is_public
      };
    } catch (err) {
      error.value = err.message || 'Failed to load recipe';
    } finally {
      loading.value = false;
    }
  }
});

// Show preview when markdown content changes
watch(() => form.value.description_md, (newValue) => {
  showPreview.value = !!newValue;
});

const submitForm = async () => {
  try {
    submitting.value = true;
    
    if (isEditing.value) {
      const id = parseInt(route.params.id);
      await recipeService.updateRecipe(id, form.value);
      router.push(`/recipe/${id}`);
    } else {
      const newRecipe = await recipeService.createRecipe(form.value);
      router.push(`/recipe/${newRecipe.id}`);
    }
  } catch (err) {
    error.value = err.message || 'Failed to save recipe';
    submitting.value = false;
  }
};
</script>