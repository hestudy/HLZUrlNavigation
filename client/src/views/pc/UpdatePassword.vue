<template>
    <Layout class="updatepassword">
        <Header style="background-color: white;margin-bottom: 3px;">
            <h3>HLZUrlNavigation安全中心</h3>
        </Header>
        <Content style="display: flex;">
            <div style="height: 100%;flex: 1">
                <img src="../../assets/bd-4.png" alt="" style="width: 100%;height: 100%;">
            </div>
            <div style="height: 100%;flex: 1;display: flex;align-items: center;justify-content: center;">
                <Card title="密码修改" style="width: 60%">
                    <Form :model="updatefrom" :label-width="80" label-position="left" :disabled="disabledupdate">
                        <FormItem label="用户名">
                            <Input v-model="updatefrom.user" placeholder="请输入用户名"></Input>
                        </FormItem>
                        <FormItem label="邮箱">
                            <Input v-model="updatefrom.email" placeholder="请输入绑定的邮箱"></Input>
                        </FormItem>
                    </Form>
                    <div style="height: 50px;width: 100%;display: flex;align-items: center;justify-content: center;">
                        <Button type="error" @click="auth()">身份验证</Button>
                    </div>
                    <div style="width: 100%;" v-show="showupdate">
                        <Form :model="updatefrom" :label-width="80" label-position="left">
                            <FormItem label="更改密码">
                                <Input v-model="updatefrom.password" placeholder="请输入新密码"></Input>
                            </FormItem>
                        </Form>
                        <div style="width:100%;height: 50px;display: flex;align-items: center;justify-content: center;">
                            <Button type="success" @click="updatepassword()">修改密码</Button>
                        </div>
                    </div>
                </Card>
            </div>
        </Content>
    </Layout>
</template>

<script>
    import httpaxios from "../../unites/httpaxios";
    export default {
        name: "UpdatePassword",
        data(){
            return{
                updatefrom:{
                    user:'',
                    email:'',
                    password:''
                },
                showupdate:false,
                disabledupdate:false
            }
        },
        methods:{
            updatepassword(){
                if(this.updatefrom.password==''){
                    this.$Message.error('请输入新密码')
                }else{
                    let url = this.$store.state.serviceurl+'/modifypassword/'
                    let postdata = {
                        user:this.updatefrom.user,
                        password:this.updatefrom.password
                    }
                    httpaxios.post(this,url,postdata,response=>{
                        if(response.data.state=='err'){
                            this.$Modal.error({
                                title:'错误提示',
                                content:'密码修改失败'
                            })
                        }else{
                            this.$Message.success('修改成功，请重新登录')
                            localStorage.removeItem('user')
                            this.$router.back()
                        }
                    })
                }
            },
            auth(){
                if(this.updatefrom.user==''){
                    this.$Message.error('请补全信息再进行身份验证')
                }else if(this.updatefrom.email==''){
                    this.$Message.error('请补全信息再进行身份验证')
                }else{
                    let url = this.$store.state.serviceurl+'/updatepassword/'
                    let postdata = {
                        user:this.updatefrom.user,
                        email:this.updatefrom.email
                    }
                    httpaxios.post(this,url,postdata,response=>{
                        if(response.data.state=='err'){
                            this.$Modal.error({
                                title:'错误提示',
                                content:'身份验证失败'
                            })
                        }else{
                            this.$Message.success('身份验证成功，显示修改密码界面')
                            this.showupdate = true
                            this.disabledupdate = true
                        }
                    })
                }
            }
        }
    }
</script>

<style scoped>
    .updatepassword{
        width: 100%;
        height: 100%;
        position: absolute;
    }
</style>