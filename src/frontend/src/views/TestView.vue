<template>
    <button @click="redirectMicrosoft">Anmelden mit Kleinweich</button>
    <ul>
        <li v-for="post in posts" :key="post.id" data-test="post">
            {{ post.title }}
        </li>
    </ul>
</template>

<script>


export default {
    data() {
        return {
            posts: null
        }
    },
    //https://login.microsoftonline.com/c930dbcd-6b10-4cff-a628-46f5dec8a038/oauth2/v2.0/authorize?client_id=ed6fe01e-2f64-49da-bce2-ea1e08cee1dd&response_type=code&redirect_uri=https%3A%2F%2Flocalhost%3A8002&response_mode=query&scope=openid%20profile%20email
    methods: {
        redirectMicrosoft() {
            var url = new URL( 'c930dbcd-6b10-4cff-a628-46f5dec8a038/oauth2/v2.0/authorize', 'https://login.microsoftonline.com/')
            url.searchParams.append('client_id', 'ed6fe01e-2f64-49da-bce2-ea1e08cee1dd')
            url.searchParams.append('response_type', 'code')
            url.searchParams.append('grant_type', 'authorization_code')
            url.searchParams.append('redirect_uri', 'https://localhost:5173/')
            url.searchParams.append('response_mode', 'query')
            url.searchParams.append('scope', 'openid profile User.Read email offline_access')


            window.open(url.href, '_self')
        }
    }
}
</script>