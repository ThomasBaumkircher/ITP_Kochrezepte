<template>
    <button @click="getPosts">Get posts</button>
    <ul>
        <li v-for="post in posts" :key="post.id" data-test="post">
            {{ post.title }}
        </li>
    </ul>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            posts: null
        }
    },
    methods: {
        async getPosts() {
            this.posts = await axios.get('https://login.microsoftonline.com/' + 'c930dbcd-6b10-4cff-a628-46f5dec8a038' + '/oauth2/v2.0/authorize', {
                params: {
                    client_id: "ed6fe01e-2f64-49da-bce2-ea1e08cee1dd",
                    response_type: "code",
                    redirect_url: "localhost:8002",
                    response_mode: "query",
                    scope: "openid profile",
                }
            })
        }
    }
}
</script>