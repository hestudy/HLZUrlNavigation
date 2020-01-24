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
        <Content style="background-color: white;overflow: hidden">
            <transition name="fade">
                <router-view></router-view>
            </transition>
        </Content>
        <Footer style="background-color: white;text-align: center;">
            <h5>202001@<a @click="showaboutme = true">怎么学都学不会的何同学</a></h5>
        </Footer>
        <Modal v-model="showaboutme" title="关于作者" draggable>
            <Layout style="width:100%;height:300px;border-radius: 10px;overflow: hidden;">
                <Content style="overflow: auto;">
                    <Layout style="width:100%;height:300px;">
                        <Header style="background-color: white;border-bottom: 1px solid darkgray">
                            <h3>Github</h3>
                        </Header>
                        <Content style="background-color: white;display: flex;align-items: center;justify-content: center">
                            <a href="https://github.com/1467602180/HLZUrlNavigation" target="_blank"><h3>https://github.com/1467602180/HLZUrlNavigation</h3></a>
                        </Content>
                    </Layout>
                    <Layout style="width:100%;height:300px;">
                        <Header style="background-color: white;border-bottom: 1px solid darkgray">
                            <h3>WeChat</h3>
                        </Header>
                        <Content style="background-color: white;display: flex;align-items: center;justify-content: center;flex-direction: column;">
                            <img :src="$store.state.serviceurl+'/WeChatImage/'" width="200" height="200">
                            <h3>怎么学都学不会的何同学</h3>
                        </Content>
                    </Layout>
                </Content>
            </Layout>
        </Modal>
    </Layout>
</template>

<script>
    export default {
        name: "Home",
        data(){
            return{
                showaboutme:false
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