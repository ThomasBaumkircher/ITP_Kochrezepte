import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProfileView from '../views/ProfileView.vue'
import TestView from '../views/TestView.vue'
import { useAuthStore } from '../store/auth'

const routes = [
    {
        // path: '/login',
        // name: 'Login',
        // component: LoginView,
    },
    {
        path: '/profile',
        name: 'Profile',
        component: ProfileView,
        meta: { requiresAuth: true },
    },

    {
        path: '/',
        name: 'Index',
        component: HomeView,
    },
    {
        path: '/login',
        name: 'Login',
        component: TestView,
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