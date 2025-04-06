// Mock user data
const currentUser = {
  email: 'user@example.com'
};

// Initial mock data
let recipes = [
  {
    id: 1,
    name: 'Spaghetti Carbonara',
    description_short: 'Classic Italian pasta dish',
    description_md: '# Spaghetti Carbonara\n\n## Ingredients\n- 400g spaghetti\n- 200g pancetta\n- 4 egg yolks\n- 50g pecorino cheese\n- 50g parmesan\n- Black pepper\n\n## Instructions\n1. Cook pasta until al dente\n2. Fry pancetta until crispy\n3. Mix eggs and cheese in a bowl\n4. Combine everything and serve',
    creator: 'user@example.com',
    is_public: true,
    created_at: '2023-01-01T12:00:00Z',
    updated_at: '2023-01-01T12:00:00Z'
  },
  {
    id: 2,
    name: 'Chocolate Chip Cookies',
    description_short: 'Classic homemade cookies',
    description_md: '# Chocolate Chip Cookies\n\n## Ingredients\n- 250g flour\n- 200g butter\n- 200g brown sugar\n- 100g white sugar\n- 2 eggs\n- 1 tsp vanilla extract\n- 200g chocolate chips\n\n## Instructions\n1. Cream butter and sugars\n2. Add eggs and vanilla\n3. Mix in dry ingredients\n4. Fold in chocolate chips\n5. Bake at 180°C for 10-12 minutes',
    creator: 'another@example.com',
    is_public: true,
    created_at: '2023-01-02T12:00:00Z',
    updated_at: '2023-01-02T12:00:00Z'
  },
  {
    id: 3,
    name: 'Private Recipe',
    description_short: 'This is a private recipe',
    description_md: 'Private content',
    creator: 'user@example.com',
    is_public: false,
    created_at: '2023-01-03T12:00:00Z',
    updated_at: '2023-01-03T12:00:00Z'
  }
];

// Helper function to generate timestamps
const generateTimestamp = () => new Date().toISOString();

// Helper function to generate new ID
const generateId = () => {
  return Math.max(0, ...recipes.map(recipe => recipe.id)) + 1;
};

export const recipeService = {
  // Get all recipes (public or owned by current user)
  async getAllRecipes() {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 300));
    
    return recipes.filter(recipe => recipe.is_public || recipe.creator === currentUser.email);
  },
  
  // Get a specific recipe
  async getRecipe(id) {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 300));
    
    const recipe = recipes.find(r => r.id === id);
    
    if (!recipe) {
      throw new Error('Recipe not found');
    }
    
    if (!recipe.is_public && recipe.creator !== currentUser.email) {
      throw new Error('Forbidden');
    }
    
    return recipe;
  },
  
  // Create a new recipe
  async createRecipe(recipeData) {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 300));
    
    const now = generateTimestamp();
    const newRecipe = {
      ...recipeData,
      id: generateId(),
      creator: currentUser.email,
      created_at: now,
      updated_at: now
    };
    
    recipes.push(newRecipe);
    return newRecipe;
  },
  
  // Update an existing recipe
  async updateRecipe(id, recipeData) {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 300));
    
    const index = recipes.findIndex(r => r.id === id);
    
    if (index === -1) {
      throw new Error('Recipe not found');
    }
    
    const recipe = recipes[index];
    
    if (recipe.creator !== currentUser.email) {
      throw new Error('Forbidden');
    }
    
    const updatedRecipe = {
      ...recipe,
      ...recipeData,
      updated_at: generateTimestamp()
    };
    
    recipes[index] = updatedRecipe;
    return updatedRecipe;
  },
  
  // Delete a recipe
  async deleteRecipe(id) {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 300));
    
    const index = recipes.findIndex(r => r.id === id);
    
    if (index === -1) {
      throw new Error('Recipe not found');
    }
    
    const recipe = recipes[index];
    
    if (recipe.creator !== currentUser.email) {
      throw new Error('Forbidden');
    }
    
    recipes.splice(index, 1);
    return { detail: 'Deleted' };
  }
};