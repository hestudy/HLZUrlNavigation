<template>
    <div class="ResourcesManageUpdateView">
        <div style="width: 500px;height: 100%;background-color: white;box-shadow: 1px 1px 3px darkgray;border-radius: 10px;overflow: hidden;">
            <Layout style="width: 100%;height: 100%;">
                <Header style="background-color: white">
                    <h3>文件夹</h3>
                </Header>
                <Content style="background-color: white;border-top: 1px solid darkgray">
                    <transition name="right">
                        <CellGroup style="max-height: 80vh;overflow: auto;" v-if="showlist" @on-click="oncell">
                            <Cell :title="item.classname" v-for="(item,index) in classdata" :key="index" :name="JSON.stringify(item)">
                                <Icon type="ios-arrow-forward" slot="extra" />
                            </Cell>
                        </CellGroup>
                        <div v-else style="width: 100%;height: 100%;">
                            <Layout style="width: 100%;height: 100%;">
                                <Header style="background-color: white;">
                                    <a @click="showlist = true">
                                        <Icon type="md-arrow-back" size="30" />
                                    </a>
                                </Header>
                                <Content style="background-color: white;padding: 10px;">
                                    <Form :model="itemdata" :label-width="80" label-position="left">
                                        <FormItem label="文件名">
                                            <Input v-model="itemdata.classname" placeholder="Enter something..."></Input>
                                        </FormItem>
                                    </Form>
                                    <div style="width: 100%;height: 50px;display: flex;align-items: center;justify-content: center;">
                                        <Button type="info" @click="updateclassname()">
                                            保存修改
                                        </Button>
                                    </div>
                                </Content>
                            </Layout>
                        </div>
                    </transition>
                </Content>
            </Layout>
        </div>
        <div style="width: 500px;height: 100%;background-color: white;box-shadow: 1px 1px 3px darkgray;border-radius: 10px;overflow: hidden;margin-left: 10px;">
            <Layout style="width: 100%;height: 100%;">
                <Header style="background-color: white">
                    <h3>资源</h3>
                </Header>
                <Content style="background-color: white;border-top: 1px solid darkgray">
                    <transition name="right">
                        <CellGroup style="max-height: 80vh;overflow: auto;" v-if="showlists" @on-click="oncells">
                            <Cell :title="item.title" v-for="(item,index) in urlsdata" :key="index" :name="JSON.stringify(item)" :label="item.href">
                                <Icon type="ios-arrow-forward" slot="extra" />
                            </Cell>
                        </CellGroup>
                        <div v-else style="width: 100%;height: 100%;">
                            <Layout style="width: 100%;height: 100%;">
                                <Header style="background-color: white;">
                                    <a @click="showlists = true">
                                        <Icon type="md-arrow-back" size="30" />
                                    </a>
                                </Header>
                                <Content style="background-color: white;padding: 10px;display: flex;flex-direction: column">
                                    <div style="width:100%;flex:1;padding: 10px;display: flex;align-items: center;justify-content: center;">
                                        <img :src="$store.state.serviceurl+'/'+itemdatas.image" style="height: 150px;width: 150px;border-radius: 50%;margin-right: 10px">
                                    </div>
                                    <div style="width:100%;flex:3">
                                        <Form :model="itemdatas" :label-width="80" label-position="left">
                                            <FormItem label="标题">
                                                <Input v-model="itemdatas.title" placeholder="输入标题"></Input>
                                            </FormItem>
                                            <FormItem label="描述">
                                                <Input v-model="itemdatas.subtitle" placeholder="输入描述"></Input>
                                            </FormItem>
                                            <FormItem label="链接">
                                                <Input v-model="itemdatas.href" placeholder="输入链接"></Input>
                                            </FormItem>
                                            <FormItem label="资源分类">
                                                <Select v-model="itemdatas.href_class_id">
                                                    <Option :value="item.id" v-for="(item,index) in classdata" :key="index">{{item.classname}}</Option>
                                                </Select>
                                            </FormItem>
                                        </Form>
                                        <div style="width: 100%;height: 50px;display: flex;align-items: center;justify-content: center;">
                                            <Button type="info" @click="updateurls">保存修改</Button>
                                        </div>
                                    </div>
                                </Content>
                            </Layout>
                        </div>
                    </transition>
                </Content>
            </Layout>
        </div>
    </div>
</template>

<script>
    import httpaxios from "../../../unites/httpaxios";

    export default {
        name: "ResourcesManageUpdateView",
        data(){
            return{
                classdata:[],
                showlist:true,
                itemdata:{},
                showlists:true,
                itemdatas:{},
                urlsdata:[]
            }
        },
        methods:{
            updateurls(){
                if(this.itemdatas.title==''||this.itemdatas.subtitle==''||this.itemdatas.href==''||this.itemdatas.href_class_id==''){
                    this.$Message.error('请补全信息')
                }else{
                    let url = this.$store.state.serviceurl+'/UpdatePrivateResources/'
                    let postdata = {
                        id:this.itemdatas.id,
                        title:this.itemdatas.title,
                        subtitle:this.itemdatas.subtitle,
                        href:this.itemdatas.href,
                        href_class:this.itemdatas.href_class_id
                    }
                    httpaxios.post(this,url,postdata,response=>{
                        if(response.data.state=='err'){
                            this.$Modal.error({
                                title:'错误提示',
                                content:'身份校验失败或该用户不存在该资源'
                            })
                        }else{
                            this.$Message.success('修改成功')
                            this.geturlsdata()
                        }
                    })
                }
            },
            updateclassname(){
                if(this.itemdata.classname==''){
                    this.$Message.error('请补全信息')
                }else{
                    let url = this.$store.state.serviceurl+'/UpdatePrivateResourcesClass/'
                    let postdata = {
                        id:this.itemdata.id,
                        classname:this.itemdata.classname
                    }
                    httpaxios.post(this,url,postdata,response=>{
                        if(response.data.state=='err'){
                            this.$Modal.error({
                                title:'错误提示',
                                content:'身份校验失败或存在同名导致修改失败'
                            })
                        }else{
                            this.$Message.success('修改成功')
                            this.getclassdata()
                        }
                    })
                }
            },
            oncells(name){
                this.showlists = false
                this.itemdatas = JSON.parse(name)
            },
            oncell(name){
                this.showlist = false
                this.itemdata = JSON.parse(name)
            },
            getclassdata(){
                let url = this.$store.state.serviceurl+'/privateresourcesclass/'
                httpaxios.get(this,url,response=>{
                    if(response.data.state=='err'){
                        this.$Modal.error({
                            title:'错误提示',
                            content:'身份校验失败'
                        })
                    }else{
                        this.classdata = response.data.data
                    }
                })
            },
            geturlsdata(){
                let url = this.$store.state.serviceurl+'/geturlsdata/'
                httpaxios.get(this,url,response=>{
                    if(response.data.state=='err'){
                        this.$Modal.error({
                            title:'错误提示',
                            content:'身份校验失败'
                        })
                    }else{
                        this.urlsdata = response.data.data
                    }
                })
            }
        },
        mounted() {
            this.getclassdata()
            this.geturlsdata()
        }
    }
</script>

<style scoped>
    .ResourcesManageUpdateView{
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 10px;
    }
</style>