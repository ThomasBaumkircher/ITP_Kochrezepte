<template>
    <div class="row d-flex justify-content-center mx-auto mt-5">
        <div class="col-6 pt-6">
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { useRoute } from 'vue-router';
import { useCookies } from 'vue-cookies';

export default {
    data() {
        return {
            posts: null
        }

    },

    async beforeMount() {
        try {
            const route = useRoute();
            console.log(route.query.code);

            const response = await axios.post('https://login.microsoftonline.com/c930dbcd-6b10-4cff-a628-46f5dec8a038/oauth2/v2.0/token', {
                client_id: 'ed6fe01e-2f64-49da-bce2-ea1e08cee1dd',
                grant_type: 'authorization_code',
                code: route.query.code,
                redirect_uri: 'https://localhost:8002/',
                client_secret: '.Af8Q~olnPQochvWqHIPSDHgQXnCKESActf04cLn',
                scope: 'openid profile email'
            }, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            });
            console.log(response.data);
            // set cookie
            document.cookie = 'access_token=' + response.data.access_token;

            axios.defaults.headers.common['Authorization'] = 'Baerer ' + response.data.access_token;
            const response2 = await axios.get('https://graph.microsoft.com//v1.0/me/email');
        } catch (error) {
            console.error(error);
        }
    }
}



</script>