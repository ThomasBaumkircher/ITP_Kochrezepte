<template>
    <div class="row d-flex justify-content-center mx-auto mt-5">
        <div class="col-6 pt-6">
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { useRoute } from 'vue-router';
import { jwtDecode } from "jwt-decode";

export default {
    data() {
        return {
            posts: null
        }

    },

    async beforeMount() {
        try {
            const route = useRoute();

            const response = await axios.post('https://login.microsoftonline.com/c930dbcd-6b10-4cff-a628-46f5dec8a038/oauth2/v2.0/token', {
                client_id: 'ed6fe01e-2f64-49da-bce2-ea1e08cee1dd',
                grant_type: 'authorization_code',
                code: route.query.code,
                redirect_uri: 'https://localhost:5173/',
                client_secret: '.Af8Q~olnPQochvWqHIPSDHgQXnCKESActf04cLn',
                scope: 'openid profile User.Read email offline_access',
            }, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            });
            // set cookie
            document.cookie = 'access_token=' + response.data.access_token;

            const data = jwtDecode(response.data.access_token);
            document.cookie = 'username=' + data.name;
            document.cookie = 'email=' + data.unique_name;

            axios.defaults.headers.common['Authorization'] = 'Baerer ' + response.data.access_token;
        } catch (error) {
            console.error(error);
        }
    }
}



</script>