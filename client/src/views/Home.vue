<template>

</template>

<script>
    export default {
        name: "Home",
        created() {
            let flag=navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i)
                if(flag){
                    this.$router.replace({name:'home-phone'})
                }else{
                    this.$router.replace({name:'home-pc'})
                }
        }
    }
</script>

<style scoped>

</style>