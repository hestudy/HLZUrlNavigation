<template>
    <div class="phone">
        <van-nav-bar>
            <van-icon name="apps-o" slot="left" size="24" @click="showpop = true" />
            <h4 slot="title">HLZUrlNavigation</h4>
        </van-nav-bar>
        <div style="width: 100%;flex: 1">
            <router-view></router-view>
        </div>
        <van-tabbar v-model="active" route>
            <van-tabbar-item icon="points" replace :to="{name:'PublicResources-phone'}">公共资源库</van-tabbar-item>
            <van-tabbar-item icon="friends-o" replace :to="{name:'UserShare-phone'}">用户分享库</van-tabbar-item>
            <van-tabbar-item icon="bag-o" replace :to="{name:'PrivateResources-phone'}">私人资源库</van-tabbar-item>
            <van-tabbar-item icon="completed" replace :to="{name:'About-phone'}">关于</van-tabbar-item>
        </van-tabbar>
        <div v-if="showpop">
            <van-popup v-model="showpop" round position="bottom" style="height:20%;display: flex;align-items: center;justify-content: center;flex-direction: column" >
                <Button type="error" @click="logout()">退出登录</Button>
                <Button type="info" style="margin-top: 10px;" @click="showtell()">差异说明</Button>
            </van-popup>
        </div>
    </div>
</template>

<script>
    import httpaxios from "../../unites/httpaxios";

    export default {
        name: "Home",
        data(){
            return{
                active:-1,
                showpop:false
            }
        },
        methods:{
            showtell(){
                this.$dialog.alert({
                    title:'关于手机版的差异说明',
                    message:'手机版没有资源管理中心，故无法对私人资源进行增删改'
                })
            },
            logout(){
                let url = this.$store.state.serviceurl+'/logout/'
                httpaxios.get(this,url,response=>{
                    this.$toast.success('注销成功，即将刷新界面')
                    localStorage.removeItem('user')
                    this.$router.go(0)
                })
            }
        }
    }
</script>

<style scoped>
    .phone{
        width: 100%;
        height: 100%;
        position: absolute;
        display: flex;
        flex-direction: column;
    }
</style>