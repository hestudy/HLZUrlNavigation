<template>
    <div class="PrivateResources" v-if="havelogin" style="display: flex">
        <van-sidebar v-model="activeKey" v-if="classdata.length==0">
            <div style="width: 100%;height: 100%;display: flex;align-items: center;justify-content: center;border-right:1px solid darkgray">
                <h5>暂无数据</h5>
            </div>
        </van-sidebar>
        <van-sidebar v-model="activeKey" style="overflow: auto;max-height: 85vh" v-else @change="changesidebar">
            <van-sidebar-item :title="item.classname" v-for="(item,index) in classdata" :key="index"/>
        </van-sidebar>
        <div style="height: 100%;flex: 1">
            <div v-if="activeKey==-1" style="width:100%;height:100%;display:flex;align-items: center;justify-content: center;padding: 10px">
                <h3>欢迎来到私人资源库，这里是专属于你的资源空间</h3>
            </div>
            <div v-else-if="urlsdata.length==0" style="width: 100%;height: 100%;display: flex;align-items: center;justify-content: center">
                <h5>暂无数据</h5>
            </div>
            <div v-else style="width: 100%;height: 100%;display: flex;flex-direction: column;align-items: center;overflow: auto;max-height: 80vh;">
                <a style="width: 90%;height: 100px;margin-top: 10px;" v-for="(item,index) in urlsdata" :key="index" @click="showdia(item)">
                    <div style="border: 1px solid darkgray;border-radius: 5px;overflow: hidden;box-shadow: 1px 1px 1px darkgray;display:flex;width: 100%;height: 100%;">
                        <div style="height:100%;flex:1;display: flex;align-items: center;justify-content: center;">
                            <img :src="$store.state.serviceurl+'/'+item.image" style="width: 90%;height: auto;border-radius: 50%;">
                        </div>
                        <div style="height:100%;flex:2;display: flex;align-items: center;justify-content: center;flex-direction: column;padding-left: 10px;padding-right: 10px;overflow: auto;max-height: 20vh">
                            <h4>{{item.title}}</h4>
                            <h5>{{item.subtitle}}</h5>
                        </div>
                    </div>
                </a>
            </div>
        </div>
        <van-dialog v-model="showdialog" :title="showdata.title" show-cancel-button confirmButtonText="进入网站" @confirm="tourls()">
            <div style="width:100%;height:50vh;display: flex;flex-direction: column;">
                <div style="width:100%;flex:1;display: flex;align-items: center;justify-content: center;">
                    <img :src="$store.state.serviceurl+'/'+this.showdata.image" style="height: 90%;width: auto;border-radius: 50%;max-width:50vw">
                </div>
                <div style="width:100%;flex:2;display: flex;flex-direction: column;align-items: center;justify-content: center;overflow: auto;max-height: 20vh;padding-left: 10px;padding-right: 10px;">
                    <h4>{{showdata.title}}</h4>
                    <h5>{{showdata.subtitle}}</h5>
                </div>
                <div style="width:100%;flex:1">
                    <van-cell center title="是否分享">
                        <van-switch v-model="showdata.share" slot="right-icon" size="24" @change="changeswitch" />
                    </van-cell>
                </div>
            </div>
        </van-dialog>
    </div>
    <div class="PrivateResources" v-else style="display: flex;align-items: center;justify-content: center;">
        <div style="width: 85%;height: 60vh;border: 1px solid darkgray;border-radius: 10px;box-shadow: 1px 1px 1px darkgray;overflow: hidden" v-if="showlogin">
            <Layout style="width:100%;height:100%;">
                <Header style="background-color: white;text-align: center;">
                    <h3>用户登录</h3>
                </Header>
                <Content style="background-color: white;display: flex;align-items: center;justify-content: center">
                    <Form :model="loginform" :label-width="60" label-position="left">
                        <FormItem label="用户名">
                            <Input v-model="loginform.user" placeholder="输入用户名"></Input>
                        </FormItem>
                        <FormItem label="密码">
                            <Input v-model="loginform.password" placeholder="输入密码" type="password" password></Input>
                        </FormItem>
                    </Form>
                </Content>
                <Footer style="background:white;display: flex;align-items: center;justify-content: center">
                    <Button type="info" @click="login()">登录</Button>
                    <Button type="warning" style="margin-left: 10px;" @click="showlogin = false">去注册</Button>
                    <Button type="error" style="margin-left: 10px;" @click="$router.push({name:'UpdatePassWord-phone'})">忘记密码</Button>
                </Footer>
            </Layout>
        </div>
        <div v-else style="width: 85%;height: 60vh;border: 1px solid darkgray;border-radius: 10px;box-shadow: 1px 1px 1px darkgray;overflow: hidden">
            <Layout style="width:100%;height:100%;">
                <Header style="background-color: white;text-align: center;">
                    <h3>用户注册</h3>
                </Header>
                <Content style="background-color: white;display: flex;align-items: center;justify-content: center">
                    <Form :model="resignform" :label-width="60" label-position="left">
                        <FormItem label="用户名">
                            <Input v-model="resignform.user" placeholder="输入用户名"></Input>
                        </FormItem>
                        <FormItem label="邮箱">
                            <Input v-model="resignform.email" placeholder="输入邮箱"></Input>
                        </FormItem>
                        <FormItem label="密码">
                            <Input v-model="resignform.password" placeholder="输入密码" type="password" password></Input>
                        </FormItem>
                    </Form>
                </Content>
                <Footer style="background:white;display: flex;align-items: center;justify-content: center">
                    <Button type="info" @click="resign()">注册</Button>
                    <Button type="warning" style="margin-left: 10px;" @click="showlogin = true">去登录</Button>
                </Footer>
            </Layout>
        </div>
    </div>
</template>

<script>
    import httpaxios from "../../../unites/httpaxios";

    export default {
        name: "PrivateResources",
        data(){
            return{
                havelogin:false,
                showlogin:true,
                activeKey:-1,
                classdata:[],
                urlsdata:[],
                showdata:{},
                showdialog:false,
                loginform:{
                    user:'',
                    password:''
                },
                resignform:{
                    user:'',
                    email:'',
                    password:''
                }
            }
        },
        methods:{
            tourls(){
                window.open(this.showdata.href,'_blank')
            },
            changeswitch(val){
                let url = this.$store.state.serviceurl+'/changeshare/'
                let postdata = {
                    id:this.showdata.id,
                    share:val
                }
                httpaxios.post(this,url,postdata,response=>{
                    if(response.data.state=='err'){
                        this.$toast.fail('身份校验失败，请刷新后重新登录')
                        localStorage.removeItem('user')
                    }else{
                        this.$toast.success('改变成功')
                    }
                })
            },
            showdia(item){
                this.showdata = item
                this.showdialog = true
            },
            changesidebar(index){
                let url = this.$store.state.serviceurl+'/privateresources/'
                let postdata = {
                    id:this.classdata[index].id
                }
                httpaxios.post(this,url,postdata,response=>{
                    if(response.data.state=='err'){
                        this.$toast.fail('身份校验失败，请刷新后重新登录')
                        localStorage.removeItem('user')
                    }else{
                        this.urlsdata = response.data.data
                    }
                })
            },
            resign(){
                if(this.resignform.user==''){
                    this.$toast.fail('请补全信息进行注册')
                }else if(this.resignform.email==''){
                    this.$toast.fail('请补全信息进行注册')
                }else if(this.resignform.password==''){
                    this.$toast.fail('请补全信息进行注册')
                }else{
                    let url = this.$store.state.serviceurl+'/resign/'
                    let postdata = {
                        user:this.resignform.user,
                        email:this.resignform.email,
                        password:this.resignform.password
                    }
                    httpaxios.post(this,url,postdata,response=>{
                        if(response.data.state=='err'){
                            this.$toast.fail('注册失败，该用户名已存在')
                        }else{
                            this.$toast.success('注册成功，跳转登录')
                            this.showlogin = true
                        }
                    })
                }
            },
            login(){
                if(this.loginform.user==''){
                    this.$toast.fail('请输入用户名')
                }else if(this.loginform.password==''){
                    this.$toast.fail('请输入密码')
                }else{
                    let url = this.$store.state.serviceurl+'/login/'
                    let postdata = {
                        user:this.loginform.user,
                        password:this.loginform.password
                    }
                    httpaxios.post(this,url,postdata,response=>{
                        if(response.data.state=='err'){
                            this.$toast.fail('登录失败，用户存在或密码错误')
                        }else{
                            this.$toast.success('登录成功')
                            localStorage.setItem('user',this.loginform.user)
                            this.gethavelogin()
                        }
                    })
                }
            },
            gethavelogin(){
                let user = localStorage.getItem('user')
                if(user==''||user==undefined||user==null){
                    this.havelogin = false
                }else{
                    this.havelogin = true
                    let url = this.$store.state.serviceurl+'/privateresourcesclass/'
                    httpaxios.get(this,url,response=>{
                        if(response.data.state=='err'){
                            this.$toast.fail('身份校验失败，请刷新后重新登录')
                            localStorage.removeItem('user')
                        }else{
                            this.classdata = response.data.data
                        }
                    })
                }
            }
        },
        mounted() {
            this.gethavelogin()
        }
    }
</script>

<style scoped>
    .PrivateResources{
        width: 100%;
        height: 100%;
    }
</style>