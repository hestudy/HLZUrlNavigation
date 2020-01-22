<template>
    <Layout class="pc">
        <Header style="background-color: white;margin-bottom:3px;display: flex;">
            <a style="margin-right: 30px;" @click="tohome()"><h3>HLZUrlNavigation</h3></a>
            <Menu mode="horizontal" @on-select="onmenu" ref="menu">
                <MenuItem name="1">
                    <Icon type="logo-buffer" />
                    公共资源库
                </MenuItem>
                <MenuItem name="2">
                    <Icon type="ios-people" />
                    用户分享库
                </MenuItem>
                <MenuItem name="3">
                    <Icon type="ios-lock" />
                    私人资源库
                </MenuItem>
                <MenuItem name="4">
                    <Icon type="ios-at" />
                    关于HLZUrlNavigation
                </MenuItem>
            </Menu>
        </Header>
        <Content style="background-color: white;">
            <transition name="fade">
                <router-view></router-view>
            </transition>
        </Content>
        <Footer style="background-color: white;text-align: center;">
            <h5>202001@<a>怎么学都学不会的何同学</a></h5>
        </Footer>
    </Layout>
</template>

<script>
    export default {
        name: "Home",
        data(){
            return{

            }
        },
        methods:{
            onmenu(name){
                switch (name) {
                    case '1':{
                        this.$router.replace({name:'publicresources-pc'})
                    }break
                    case '2':{
                        this.$router.replace({name:'usershare-pc'})
                    }break
                    case '3':{
                        this.$router.replace({name:'privatesources-pc'})
                    }break
                    case '4':{
                        this.$router.replace({name:'about-pc'})
                    }break
                }
            },
            tohome(){
                this.$router.replace({name:'home-pc'})
                this.$refs.menu.currentActiveName = "0"
            }
        }
    }
</script>

<style scoped>
    .pc{
        width: 100%;
        height: 100%;
        position: absolute;
    }
    .ivu-menu{
        position: unset;
    }
</style>