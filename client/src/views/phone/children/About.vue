<template>
    <div class="About">
        <div style="width: 100%;height: 100%;display: flex;align-items: center;justify-content: center;">
            <div style="width: 90%;height: 90%;border: 1px solid darkgray;border-radius: 10px;overflow: hidden;box-shadow: 1px 1px 1px darkgray;padding: 10px;">
                <viewer :value="aboutdata.content" style="max-height: 75vh;overflow: auto;"></viewer>
            </div>
        </div>
        <div style="width: 100%;height: 100%;margin-bottom: 10px;">
            <Layout style="width:100%;height:100%;">
                <Header style="background-color: white;text-align: center">
                    <h4>用户评论区</h4>
                </Header>
                <Content style="padding-left: 10px;padding-right: 10px;">
                    <List style="overflow: auto;max-height: 65vh">
                        <ListItem v-for="(item,index) in commentsdata" :key="index">
                            <ListItemMeta>
                                <Avatar style="background-color: #87d068" icon="ios-person" slot="avatar" />
                                <h4 slot="title">用户：{{item.user}}</h4>
                                <h5 slot="description">{{item.content}}</h5>
                            </ListItemMeta>
                        </ListItem>
                    </List>
                </Content>
                <Footer style="background-color: white;display: flex;align-items: center;justify-content: center">
                    <Input placeholder="输入评论" v-model="commentscontent"/>
                    <Button type="info" style="margin-left: 10px;" @click="pushcomments()">发送</Button>
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
                aboutdata:{
                    content:''
                },
                commentscontent:'',
                commentsdata:[]
            }
        },
        methods:{
            pushcomments(){
                if(this.commentscontent==''){
                    this.$toast.fail('请输入评论内容')
                }else{
                    let url = this.$store.state.serviceurl+'/CommentsPush/'
                    let postdata = {
                        content:this.commentscontent
                    }
                    httpaxios.post(this,url,postdata,response=>{
                        if(response.data.state=='err'){
                            this.$toast.fail('请先登录')
                        }else{
                            this.$toast.success('评论成功')
                            this.commentscontent = ''
                            this.getcommentsdata()
                        }
                    })
                }
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
                this.aboutdata = response.data.data
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
        max-height: 90vh;
    }
</style>