<template>
    <Layout class="EditContent">
        <Header style="background-color: white">
            <h3>编辑关于文章</h3>
        </Header>
        <Content style="display: flex;align-items: center;justify-content: center;padding: 30px;">
            <div style="height: 100%;width: 800px;background-color: white;border-radius: 10px;box-shadow: 1px 1px 3px darkgray;overflow: hidden;display: flex;flex-direction: column">
                <editor style="width: 100%;flex: 1" v-model="aboutcontent"></editor>
            </div>
        </Content>
        <Footer style="background-color: white;display: flex;align-items: center;justify-content: center">
            <Button type="info" @click="savecontent()">
                提交
            </Button>
        </Footer>
    </Layout>
</template>

<script>
    import 'tui-editor/dist/tui-editor.css';
    import 'tui-editor/dist/tui-editor-contents.css';
    import 'codemirror/lib/codemirror.css';
    import Editor from '@toast-ui/vue-editor/src/Editor.vue'
    import httpaxios from "../../unites/httpaxios";
    export default {
        name: "EditContent",
        components: {
            'editor': Editor
        },
        data(){
            return{
                aboutcontent:''
            }
        },
        methods:{
            savecontent(){
                let url = this.$store.state.serviceurl+'/UpdateAbout/'
                let postdata = {
                    content:this.aboutcontent
                }
                httpaxios.post(this,url,postdata,response=>{
                    if(response.data.state=='err'){
                        this.$Modal.error({
                            title:'错误提示',
                            content:'非管理员无法操作'
                        })
                    }else{
                        this.$Message.success('修改成功')
                    }
                })
            }
        },
        mounted() {
            let url = this.$store.state.serviceurl+'/ReadAbout/'
            httpaxios.get(this,url,response=>{
                this.aboutcontent = response.data.data.content
            })
        }
    }
</script>

<style scoped>
    .EditContent{
        width: 100%;
        height: 100%;
        position: absolute;
    }
</style>