<template>
    <Layout class="ResourcesManageAddView">
        <Header style="background-color: white;margin-bottom: 3px;display: flex;align-items: center;justify-content: center;">
            <Menu mode="horizontal" active-name="1" @on-select="onmenu">
                <MenuItem name="1">
                    <Icon type="md-albums"/>
                    增加文件夹
                </MenuItem>
                <MenuItem name="2">
                    <Icon type="md-at"/>
                    增加资源
                </MenuItem>
            </Menu>
        </Header>
        <Content>
            <div v-if="menuactive=='1'"
                 style="width:100%;height:100%;display:flex;align-items: center;justify-content: center;">
                <div style="width:800px;height:auto;background-color: white;border-radius: 10px;box-shadow: 1px 1px 3px darkgray;display: flex;align-items: center;justify-content: center;flex-direction: column;padding: 30px;">
                    <Form :model="PrivateResourcesClassFrom" :label-width="100" label-position="left">
                        <FormItem label="新增文件夹">
                            <Input v-model="PrivateResourcesClassFrom.classname" placeholder="新增文件夹名"></Input>
                        </FormItem>
                    </Form>
                    <div style="width: 100%;height: 50px;display: flex;align-items: center;justify-content: center;">
                        <Button type="info" @click="savePrivateResourcesClass()">
                            提交
                        </Button>
                    </div>
                </div>
            </div>
            <div v-else style="width:100%;height:100%;display:flex;align-items: center;justify-content: center;">
                <div style="width:800px;height:auto;background-color: white;border-radius: 10px;box-shadow: 1px 1px 3px darkgray;display: flex;align-items: center;justify-content: center;flex-direction: column;padding: 30px;">
                    <Form :model="PrivateResourcesFrom" :label-width="100" label-position="left">
                        <FormItem label="标题">
                            <Input v-model="PrivateResourcesFrom.title" placeholder="新增资源标题"></Input>
                        </FormItem>
                        <FormItem label="描述">
                            <Input v-model="PrivateResourcesFrom.subtitle" placeholder="新增资源描述"></Input>
                        </FormItem>
                        <FormItem label="链接">
                            <Input v-model="PrivateResourcesFrom.href" placeholder="新增资源链接"></Input>
                        </FormItem>
                        <FormItem label="资源分类">
                            <Select v-model="PrivateResourcesFrom.href_class">
                                <Option :value="item.classname" v-for="(item,index) in href_classdata" :key="index">
                                    {{item.classname}}
                                </Option>
                            </Select>
                        </FormItem>
                    </Form>
                    <div style="width: 100%;height: 100px;padding: 10px;display: flex;align-items: center;justify-content: center;">
                        <van-uploader :after-read="afterRead" />
                        <img :src="PrivateResourcesFrom.image.content" v-if="PrivateResourcesFrom.image!=null" style="height: 80px;width:80px;margin-left: 10px;box-shadow: 1px 1px 3px darkgray;">
                    </div>
                    <div style="width: 100%;height: 50px;display: flex;align-items: center;justify-content: center;">
                        <Button type="info" @click="savePrivateResources()">
                            提交
                        </Button>
                    </div>
                </div>
            </div>
        </Content>
    </Layout>
</template>

<script>
    import httpaxios from "../../../unites/httpaxios";

    export default {
        name: "ResourcesManageAddView",
        data() {
            return {
                menuactive: "1",
                PrivateResourcesClassFrom: {
                    classname: ''
                },
                PrivateResourcesFrom: {
                    title: '',
                    subtitle: '',
                    href: '',
                    href_class: '',
                    image:null
                },
                href_classdata: []
            }
        },
        methods: {
            afterRead(file) {
                this.PrivateResourcesFrom.image = file
            },
            savePrivateResources() {
                if (this.PrivateResourcesFrom.title == '') {
                    this.$Message.error('请补全信息再添加资源')
                } else if (this.PrivateResourcesFrom.subtitle == '') {
                    this.$Message.error('请补全信息再添加资源')
                } else if (this.PrivateResourcesFrom.href == '') {
                    this.$Message.error('请补全信息再添加资源')
                } else if (this.PrivateResourcesFrom.href_class == '') {
                    this.$Message.error('请补全信息再添加资源')
                } else if (this.PrivateResourcesFrom.image == null) {
                    this.$Message.error('请补全信息再添加资源')
                } else {
                    let url = this.$store.state.serviceurl + '/AddPrivateResources/'
                    let postdata = new FormData()
                    postdata.append('title', this.PrivateResourcesFrom.title)
                    postdata.append('subtitle', this.PrivateResourcesFrom.subtitle)
                    postdata.append('href', this.PrivateResourcesFrom.href)
                    postdata.append('href_class', this.PrivateResourcesFrom.href_class)
                    postdata.append('image', this.PrivateResourcesFrom.image.file)
                    this.$Spin.show()
                    this.$axios.post(url, postdata)
                        .then(response => {
                            if (response.data.state == 'err') {
                                this.$Modal.error({
                                    title: '错误提示',
                                    content: '身份校验失败或已存在相同链接的资源'
                                })
                            } else {
                                this.$Message.success('添加成功')
                                this.PrivateResourcesFrom = {
                                    title: '',
                                    subtitle: '',
                                    href: '',
                                    href_class: '',
                                    image:null
                                }
                            }
                        })
                    .catch(err=>{
                        console.log(err)
                        console.log(err)
                        this.$Modal.error({
                            title:'错误提示',
                            content:'很抱歉，网络请求失败，请稍后再试'
                        })
                    })
                    .finally(()=>{
                        this.$Spin.hide()
                    })
                }
            },
            savePrivateResourcesClass() {
                if (this.PrivateResourcesClassFrom.classname == '') {
                    this.$Modal.error({
                        title: '错误提示',
                        content: '请输入新文件夹名'
                    })
                } else {
                    let url = this.$store.state.serviceurl + '/AddPrivateResourcesClass/'
                    let postdata = {
                        add: this.PrivateResourcesClassFrom.classname
                    }
                    httpaxios.post(this, url, postdata, response => {
                        if (response.data.state == 'err') {
                            this.$Message.error('新建失败，该文件夹已存在或身份校验失败')
                        } else {
                            this.$Message.success('新建成功')
                            this.PrivateResourcesClassFrom.classname = ''
                            this.getclassdata()
                        }
                    })
                }
            },
            onmenu(name) {
                this.menuactive = name
            },
            getclassdata(){
                let url = this.$store.state.serviceurl + '/privateresourcesclass/'
                httpaxios.get(this, url, response => {
                    if (response.data.state == 'err') {
                        this.$Modal.error({
                            title: '错误提示',
                            content: '身份校验失败'
                        })
                    } else {
                        this.href_classdata = response.data.data
                    }
                })
            }
        },
        mounted() {
            this.getclassdata()
        }
    }
</script>

<style scoped>
    .ResourcesManageAddView {
        width: 100%;
        height: 100%;
    }

    .ivu-menu {
        position: unset;
    }
</style>