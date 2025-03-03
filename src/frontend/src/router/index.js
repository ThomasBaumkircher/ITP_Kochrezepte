import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import TestView from '../views/TestView.vue'
import RegisterView from '../views/RegisterView.vue'
import { useAuthStore } from '../store/auth'

const routes = [
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
    },
    {
        path: '/logout',
        name: 'Logout',
        component: LogoutView,
    },
    {
        path: '/register',
        name: 'Register',
        component: RegisterView,
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