<template>
    <Layout class="UpdatePassWord">
        <Header style="text-align: center">
            <h4 style="color: white">HLZUrlNavigation安全中心</h4>
        </Header>
        <Content style="width: 100%;height: 100%;display: flex;align-items: center;justify-content: center">
            <div style="width: 90%;height: auto;background-color: white;padding: 10px;border-radius: 10px;box-shadow: 1px 1px 1px darkgray">
                <Form :model="formItem" :label-width="80">
                    <FormItem label="用户名">
                        <Input v-model="formItem.user" placeholder="输入用户名"></Input>
                    </FormItem>
                    <FormItem label="邮箱">
                        <Input v-model="formItem.email" placeholder="输入该用户名绑定的邮箱"></Input>
                    </FormItem>
                    <FormItem label="新密码">
                        <Input v-model="formItem.password" placeholder="输入新密码" type="password" password></Input>
                    </FormItem>
                </Form>
            </div>
        </Content>
        <Footer style="background-color: white;display: flex;align-items: center;justify-content: center">
            <Button type="info" @click="updatepassword()">提交</Button>
        </Footer>
    </Layout>
</template>

<script>
    import httpaxios from "../../unites/httpaxios";

    export default {
        name: "UpdatePassWord",
        data(){
            return{
                formItem:{
                    user:'',
                    email:'',
                    password:''
                }
            }
        },
        methods:{
            updatepassword(){
                if(this.formItem.user==''){
                    this.$toast.fail('请补全信息')
                }else if(this.formItem.email==''){
                    this.$toast.fail('请补全信息')
                }else if(this.formItem.password==''){
                    this.$toast.fail('请补全信息')
                }else{
                    let url = this.$store.state.serviceurl+'/updatepassword/'
                    let postdata = {
                        user:this.formItem.user,
                        email:this.formItem.email
                    }
                    httpaxios.post(this,url,postdata,response=>{
                        if(response.data.state=='err'){
                            this.$toast.fail('账号信息不符合')
                        }else{
                            let url = this.$store.state.serviceurl+'/modifypassword/'
                            let postdata = {
                                user:this.formItem.user,
                                password:this.formItem.password
                            }
                            httpaxios.post(this,url,postdata,response=>{
                                if(response.data.state=='err'){
                                    this.$toast.fail('修改失败')
                                }else{
                                    this.$toast.success('修改成功')
                                }
                            })
                        }
                    })
                }
            }
        }
    }
</script>

<style scoped>
    .UpdatePassWord{
        width: 100%;
        height: 100%;
        position: absolute;
    }
</style>