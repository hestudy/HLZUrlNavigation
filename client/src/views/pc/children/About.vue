<template>
    <div class="About">
        <div style="width: 100%;height: 100%;display: flex;align-items: center;justify-content: center;flex-direction: column">
            <Button type="info" @click="editcontent()">编辑</Button>
            <div style="width: 800px;height: 70vh;border: 1px solid darkgray;border-radius: 10px;overflow: hidden;box-shadow: 1px 1px 3px darkgray;padding: 10px;margin-top: 10px;">
                <viewer :value="aboutcontent" style="max-height: 69vh;overflow: auto;"></viewer>
            </div>
        </div>
        <div style="width: 100%;height: 100%">
            <Layout style="width: 100%;height: 100%;">
                <Header style="background-color: white;border-bottom: 1px solid darkgray">
                    <h3>用户评论区</h3>
                </Header>
                <Content style="background-color: white;padding-left: 30px;padding-right: 30px;overflow: auto;max-height: 80vh">
                    <List>
                        <ListItem v-for="(item,index) in commentsdata" :key="index">
                            <ListItemMeta>
                                <Avatar style="background-color: #87d068" icon="ios-person" slot="avatar" />
                                <h3 slot="title">用户：{{item.user}}</h3>
                                <h5 slot="description">{{item.content}}</h5>
                            </ListItemMeta>
                        </ListItem>
                    </List>
                </Content>
                <Footer style="display: flex;align-items: center;justify-content: center;">
                    <Input placeholder="请输入评论" v-model="commentscontent" />
                    <Button type="info" style="margin-left: 30px;" @click="pushcomments()">发送</Button>
                </Footer>
            </Layout>
        </div>
    </div>
</template>

<script>
    import 'tui-editor/dist/tui-editor-contents.css';
    import 'highlight.js/styles/github.css';
    import Viewer from '@toast-ui/vue-editor/src/Viewer.vue'
    import httpaxios from "../../../unites/httpaxios";
    export default {
        name: "About",
        components: {
            'viewer': Viewer
        },
        data(){
            return{
                aboutcontent:'',
                commentscontent:'',
                commentsdata:[]
            }
        },
        methods:{
            pushcomments(){
                if(this.commentscontent==''){
                    this.$Message.error('请输入评论')
                }else{
                    let url = this.$store.state.serviceurl+'/CommentsPush/'
                    let postdata = {
                        content:this.commentscontent
                    }
                    httpaxios.post(this,url,postdata,response=>{
                        if(response.data.state=='err'){
                            this.$Modal.error({
                                title:'错误提示',
                                content:'身份校验失败'
                            })
                        }else{
                            this.$Message.success('发送成功')
                            this.commentscontent = ''
                            this.getcommentsdata()
                        }
                    })
                }
            },
            editcontent(){
                let url = this.$store.state.serviceurl+'/IsSuperUser/'
                httpaxios.get(this,url,response=>{
                    if(response.data.state=='err'){
                        this.$Message.error('您非管理员，无法进行此操作')
                    }else{
                        this.$router.push({name:'EditContent-pc'})
                    }
                })
            },
            getcommentsdata(){
                let url = this.$store.state.serviceurl+'/CommentsData/'
                httpaxios.get(this,url,response=>{
                    this.commentsdata = response.data.data
                })
            }
        },
        mounted() {
            let url = this.$store.state.serviceurl+'/ReadAbout/'
            httpaxios.get(this,url,response=>{
                this.aboutcontent = response.data.data.content
            })
            this.getcommentsdata()
        }
    }
</script>

<style scoped>
    .About{
        width: 100%;
        height: 100%;
        overflow: auto;
    }
</style>