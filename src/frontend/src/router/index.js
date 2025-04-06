import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import TestView from '../views/TestView.vue'
import RegisterView from '../views/RegisterView.vue'
import { useAuthStore } from '../store/auth'

import RecipeList from '../views/RecipeList.vue'
import RecipeDetail from '../views/RecipeDetail.vue'
import RecipeForm from '../views/RecipeForm.vue'


const routes = [
    {
        path: '/login',
        name: 'Login',
        component: TestView,
    },
    {
        path: '/',
        name: 'home',
        component: RecipeList
      },
      {
        path: '/recipe/:id',
        name: 'recipe-detail',
        component: RecipeDetail
      },
      {
        path: '/create',
        name: 'create-recipe',
        component: RecipeForm
      },
      {
        path: '/edit/:id',
        name: 'edit-recipe',
        component: RecipeForm
      }
]

const router = createRouter({
    history: createWebHistory(),
    routes, // short for `routes: routes`
})

router.beforeEach((to, from, next) => {
    const auth = useAuthStore();
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (auth.isAuthenticated) {
            next();
            return;
        }
        next("/login");
    } else {
        next();
    }

})

export default router;