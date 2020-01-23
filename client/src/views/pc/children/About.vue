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
                <Content style="background-color: white">

                </Content>
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
                aboutcontent:''
            }
        },
        methods:{
            editcontent(){
                let url = this.$store.state.serviceurl+'/IsSuperUser/'
                httpaxios.get(this,url,response=>{
                    if(response.data.state=='err'){
                        this.$Message.error('您非管理员，无法进行此操作')
                    }else{
                        this.$router.push({name:'EditContent-pc'})
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
    .About{
        width: 100%;
        height: 100%;
        overflow: auto;
    }
</style>