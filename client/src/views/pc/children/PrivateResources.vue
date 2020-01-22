<template>
    <Layout class="PrivateResources" v-if="!havelogin">
        <Content style="display: flex;align-items: center;justify-content: center;">
            <img src="../../../assets/bd-3.png" style="height: 100%;width: auto;z-index: 0">
            <div style="background: white;width: 40vw;height: 50vh;box-shadow: 1px 1px 3px darkgray;border-radius: 10px;z-index: 999;position:absolute;">
                <Layout style="width: 100%;height: 100%" v-if="showlogin">
                    <Header style="background: white;text-align: center;">
                        <h2>登录</h2>
                    </Header>
                    <Content style="background: white;display: flex;flex-direction: column;align-items: center;justify-content: center;">
                        <Form :model="loginfrom" :label-width="80" label-position="left">
                            <FormItem label="用户名">
                                <Input v-model="loginfrom.user" placeholder="请输入用户名"></Input>
                            </FormItem>
                            <FormItem label="密码">
                                <Input v-model="loginfrom.password" placeholder="请输入密码" type="password" password></Input>
                            </FormItem>
                        </Form>
                        <div style="height: 100px;display: flex;align-items: center;justify-content: center;">
                            <Button type="success" style="margin-right: 30px;" @click="login()">登录</Button>
                            <Button type="info" style="margin-right: 30px;" @click="toresign()">去注册</Button>
                            <Button type="error" @click="toupdatepassword()">找回密码</Button>
                        </div>
                    </Content>
                </Layout>
                <Layout style="width: 100%;height: 100%" v-else>
                    <Header style="background: white;text-align: center;">
                        <h2>注册</h2>
                    </Header>
                    <Content style="background: white;display: flex;flex-direction: column;align-items: center;justify-content: center;">
                        <Form :model="resignfrom" :label-width="80" label-position="left">
                            <FormItem label="邮箱">
                                <Input v-model="resignfrom.email" placeholder="请输入邮箱"></Input>
                            </FormItem>
                            <FormItem label="用户名">
                                <Input v-model="resignfrom.user" placeholder="请输入用户名"></Input>
                            </FormItem>
                            <FormItem label="密码">
                                <Input v-model="resignfrom.password" placeholder="请输入密码" type="password" password></Input>
                            </FormItem>
                        </Form>
                        <div style="height: 100px;display: flex;align-items: center;justify-content: center;">
                            <Button type="success" style="margin-right: 30px;" @click="resign()">注册</Button>
                            <Button type="info" @click="tologin()">去登录</Button>
                        </div>
                    </Content>
                </Layout>
            </div>
        </Content>
    </Layout>
    <Layout class="PrivateResources" v-else>
        <Header style="background: white;margin-bottom: 3px;">
            <Dropdown @on-click="ondrop">
                <a href="javascript:void(0)">
                    <Avatar style="background-color: #2D8CF1;color: white;">{{getuser()}}</Avatar>
                    <Icon type="ios-arrow-down"></Icon>
                </a>
                <DropdownMenu slot="list">
                    <DropdownItem name="1">修改密码</DropdownItem>
                    <DropdownItem name="2">退出登录</DropdownItem>
                </DropdownMenu>
            </Dropdown>
        </Header>
        <Content>
            <Layout style="width: 100%;height: 100%;">
                <Sider style="background: white">
                    <Menu style="width:100%;max-height:78vh;overflow: auto;text-align: center" @on-select="onmenu">
                        <MenuItem :name="item.id" v-for="(item,index) in classdata" :key="index">
                            {{item.classname}}
                        </MenuItem>
                    </Menu>
                </Sider>
                <Content>
                    <div v-if="menuindex==0" style="width: 100%;height: 100%;display: flex;align-items: center;justify-content: center;">
                        <h3>欢迎来到私人资源库，这里是只属于你自己的资源存储</h3>
                    </div>
                    <div v-else style="width: 100%;height: 100%;display: flex;flex-wrap: wrap;align-content: flex-start;">
                        <a style="margin: 10px;" class="urls" v-for="(item,index) in urlsdata" :key="index">
                            <div style="width: 400px;height: 200px;background-color: white;border-radius: 10px;"></div>
                        </a>
                    </div>
                </Content>
            </Layout>
        </Content>
    </Layout>
</template>

<script>
    import httpaxios from "../../../unites/httpaxios";
    import qs from 'qs'
    export default {
        name: "PrivateResources",
        data(){
            return{
                havelogin:false,
                showlogin:true,
                loginfrom:{
                    user:'',
                    password:''
                },
                resignfrom:{
                    user:'',
                    email:'',
                    password:''
                },
                classdata:[],
                menuindex:0,
                urlsdata:[]
            }
        },
        methods:{
            onmenu(name){
                this.menuindex = name
                let url = this.$store.state.serviceurl+'/privateresources/'
                let postdata = {
                    id:name
                }
                httpaxios.post(this,url,postdata,response=>{
                    if(response.data.state=='err'){
                        this.$Modal.error({
                            title:'错误提示',
                            content:'身份校验出错，请重新登录再试'
                        })
                    }else{
                        this.urlsdata = response.data.data
                    }
                })
            },
            toupdatepassword(){
                this.$router.push({name:'UpdatePassword-pc'})
            },
            resign(){
                if(this.resignfrom.email==''){
                    this.$Message.error('请补全信息再注册')
                }else if(this.resignfrom.user==''){
                    this.$Message.error('请补全信息再注册')
                }else if(this.resignfrom.password==''){
                    this.$Message.error('请补全信息再注册')
                }else{
                    let url = this.$store.state.serviceurl+'/resign/'
                    let postdata = {
                        email:this.resignfrom.email,
                        user:this.resignfrom.user,
                        password:this.resignfrom.password
                    }
                    httpaxios.post(this,url,postdata,response=>{
                        if(response.data.state=='err'){
                            this.$Modal.error({
                                title:'错误提示',
                                content:'该用户已注册'
                            })
                        }else{
                            this.$Message.success('注册成功，跳转登录界面')
                            this.showlogin = true
                        }
                    })
                }
            },
            ondrop(name){
                switch (name) {
                    case "1":{
                        this.$router.push({name:'UpdatePassword-pc'})
                    }break
                    case "2":{
                        let url = this.$store.state.serviceurl+'/logout/'
                        httpaxios.get(this,url,response=>{
                            localStorage.removeItem('user')
                            this.havelogin = false
                        })
                    }break
                }
            },
            getuser(){
                return localStorage.getItem('user')
            },
            toresign(){
                this.showlogin = false
            },
            tologin(){
                this.showlogin = true
            },
            login(){
                if(this.loginfrom.user==''){
                    this.$Message.error('请输入用户名再操作')
                }else if(this.loginfrom.password==''){
                    this.$Message.error('请输入密码再操作')
                }else{
                    let url = this.$store.state.serviceurl+'/login/'
                    let postdata = {
                        user:this.loginfrom.user,
                        password:this.loginfrom.password
                    }
                    httpaxios.post(this,url,postdata,response=>{
                        if(response.data.state=='err'){
                            this.$Modal.error({
                                title:'错误提示',
                                content:'用户名不存在或密码错误'
                            })
                        }else{
                            localStorage.setItem('user',this.loginfrom.user)
                            this.havelogin = true
                        }
                    })
                }
            }
        },
        mounted() {
            let user = localStorage.getItem('user')
            if(user!=''&&user!=null&&user!=undefined){
                this.havelogin = true
                let url = this.$store.state.serviceurl+'/privateresourcesclass/'
                let postdata = {
                    user:localStorage.getItem('user')
                }
                httpaxios.post(this,url,postdata,response=>{
                    if(response.data.state=='err'){
                        this.$Modal.error({
                            title:'错误提示',
                            content:'获取分类信息失败'
                        })
                    }else{
                        this.classdata = response.data.data
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .PrivateResources{
        width: 100%;
        height: 100%;
    }
    .ivu-menu{
        position: unset;
    }
    .urls:hover{
        box-shadow: 1px 1px 3px darkgray;
    }
</style>