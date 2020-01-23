<template>
    <div class="ResourcesManageDeleteView">
        <div style="height: 100%;flex: 1;padding: 10px;">
            <Layout style="width: 100%;height: 100%">
                <Header style="background-color: white">
                    <h3>文件夹</h3>
                </Header>
                <Content style="background-color: white;margin-top: 3px;overflow: auto;max-height: 80vh;">
                    <Table :columns="PrivateResourcesClasscolumns" :data="PrivateResourcesClass" border>
                        <template slot-scope="{ row, index }" slot="action">
                            <Button type="error" size="small" @click="removePrivateResourcesClass(index)">删除</Button>
                        </template>
                    </Table>
                </Content>
            </Layout>
        </div>
        <div style="height: 100%;flex: 1;padding: 10px;">
            <Layout style="width: 100%;height: 100%">
                <Header style="background-color: white">
                    <h3>资源</h3>
                </Header>
                <Content style="background-color: white;margin-top: 3px;overflow: auto;max-height: 80vh;">
                    <Table :columns="PrivateResourcescolumns" :data="PrivateResources" border>
                        <template slot-scope="{ row, index }" slot="action">
                            <Button type="error" size="small" @click="removePrivateResources(index)">删除</Button>
                        </template>
                    </Table>
                </Content>
            </Layout>
        </div>
    </div>
</template>

<script>
    import httpaxios from "../../../unites/httpaxios";
    export default {
        name: "ResourcesManageDeleteView",
        data(){
            return{
                PrivateResourcesClass:[],
                PrivateResources:[],
                PrivateResourcescolumns:[
                    {
                        title: '标题',
                        key:'title'
                    },
                    {
                        title: '描述',
                        key:'subtitle'
                    },
                    {
                        title: '链接',
                        key:'href'
                    },
                    {
                        title: '操作',
                        slot: 'action',
                        width: 150,
                        align: 'center'
                    }
                ],
                PrivateResourcesClasscolumns:[
                    {
                        title:'文件夹名',
                        key:'classname'
                    },
                    {
                        title:'创建时间',
                        key:'date'
                    },
                    {
                        title: '操作',
                        slot: 'action',
                        width: 150,
                        align: 'center'
                    }
                ]
            }
        },
        methods:{
            removePrivateResources(index){
                let url = this.$store.state.serviceurl+'/DeletePrivateResources/'
                let postdata = {
                    id:this.PrivateResources[index].id
                }
                httpaxios.post(this,url,postdata,response=>{
                    if(response.data.state=='err'){
                        this.$Modal.error({
                            title:'错误提示',
                            content:'身份校验失败或不存在该资源'
                        })
                    }else{
                        this.$Message.success('删除成功')
                        this.getdata()
                    }
                })
            },
            removePrivateResourcesClass(index){
                let url = this.$store.state.serviceurl+'/DeletePrivateResourcesClass/'
                let postdata = {
                    id:this.PrivateResourcesClass[index].id
                }
                httpaxios.post(this,url,postdata,response=>{
                    if(response.data.state=='err'){
                        this.$Modal.error({
                            title:'错误提示',
                            content:'身份校验失败或不存在该文件夹'
                        })
                    }else{
                        this.$Message.success('删除成功')
                        this.getdata()
                    }
                })
            },
            getdata(){
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
        },
        mounted() {
            this.getdata()
        }
    }
</script>

<style scoped>
    .ResourcesManageDeleteView{
        width: 100%;
        height: 100%;
        display: flex;
    }
</style>