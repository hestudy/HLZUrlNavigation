<template>
    <div class="ResourcesManageOverView">
        <div style="width: 450px;height: 300px;background-color: white;box-shadow: 1px 1px 3px darkgray;border-radius: 10px;overflow: hidden;margin: 10px;">
            <Layout style="width: 100%;height: 100%;">
                <Header style="background-color: white;text-align: center">
                    <h3>文件夹数量</h3>
                </Header>
                <Content style="background-color: white;display: flex;align-items: center;justify-content: center;">
                    <i-circle :percent="PrivateResourcesClass.length">
                        <span class="demo-Circle-inner" style="font-size:24px">{{PrivateResourcesClass.length}}</span>
                    </i-circle>
                </Content>
            </Layout>
        </div>
        <div style="width: 450px;height: 300px;background-color: white;box-shadow: 1px 1px 3px darkgray;border-radius: 10px;overflow: hidden;margin: 10px;">
            <Layout style="width: 100%;height: 100%;">
                <Header style="background-color: white;text-align: center">
                    <h3>资源数量</h3>
                </Header>
                <Content style="background-color: white;display: flex;align-items: center;justify-content: center;">
                    <i-circle :percent="PrivateResources.length">
                        <span class="demo-Circle-inner" style="font-size:24px">{{PrivateResources.length}}</span>
                    </i-circle>
                </Content>
            </Layout>
        </div>
    </div>
</template>

<script>
    import httpaxios from "../../../unites/httpaxios";
    export default {
        name: "ResourcesManageOverView",
        data(){
            return{
                PrivateResourcesClass:[],
                PrivateResources:[]
            }
        },
        mounted() {
            let url = this.$store.state.serviceurl+'/ResourcesManageOverView/'
            httpaxios.get(this,url,response=>{
                if(response.data.state=='err'){
                    this.$Modal.error({
                        title:'错误提示',
                        content:'身份校验不通过'
                    })
                }else{
                    this.PrivateResourcesClass = response.data.PrivateResourcesClass
                    this.PrivateResources = response.data.PrivateResources
                }
            })
        }
    }
</script>

<style scoped>
    .ResourcesManageOverView{
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        align-content: center;
    }
</style>