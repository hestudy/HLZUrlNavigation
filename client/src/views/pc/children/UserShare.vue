<template>
    <Tabs type="card" style="width: 100%;height:100%;padding:3px;" @on-click="ontabs">
        <TabPane label="按热度排序" name="1">
            <div style="width: 100%;height: 80vh;max-height: 80vh;overflow: auto;display: flex;flex-wrap: wrap;align-content: flex-start;">
                <a v-for="(item,index) in urlsdata" :key="index" @click="tourls(item)" style="margin: 30px;">
                    <div class="urls">
                        <div style="height: 100%;flex: 1;padding: 3px;display: flex;align-items: center;justify-content: center;">
                            <img :src="$store.state.serviceurl+'/'+item.image" style="width: 100%;height: auto;border-radius: 50%;">
                        </div>
                        <div style="height: 100%;flex: 2;border-left: 1px solid darkgray;">
                            <Layout style="width: 100%;height: 100%">
                                <Header style="background-color: white;text-align: center;">
                                    <h3>{{item.title}}</h3>
                                </Header>
                                <Content style="background-color: white;padding: 10px;overflow: auto;max-height: 10vh">
                                    <h5>{{item.subtitle}}</h5>
                                </Content>
                                <Footer style="background-color: white">
                                    <Icon type="md-flame" />
                                    {{item.share_hot}}
                                    <Icon type="md-calendar" style="margin-left: 10px;" />
                                    {{item.share_date}}
                                </Footer>
                            </Layout>
                        </div>
                    </div>
                </a>
            </div>
        </TabPane>
        <TabPane label="按时间排序" name="2">
            <div style="width: 100%;height: 80vh;max-height: 80vh;overflow: auto;display: flex;flex-wrap: wrap;align-content: flex-start;">
                <a v-for="(item,index) in urlsdata" :key="index" style="margin: 30px;">
                    <div class="urls">
                        <div style="height: 100%;flex: 1;padding: 3px;display: flex;align-items: center;justify-content: center;">
                            <img :src="$store.state.serviceurl+'/'+item.image" style="width: 100%;height: auto;border-radius: 50%;">
                        </div>
                        <div style="height: 100%;flex: 2;border-left: 1px solid darkgray;">
                            <Layout style="width: 100%;height: 100%">
                                <Header style="background-color: white;text-align: center;">
                                    <h3>{{item.title}}</h3>
                                </Header>
                                <Content style="background-color: white;padding: 10px;overflow: auto;max-height: 10vh">
                                    <h5>{{item.subtitle}}</h5>
                                </Content>
                                <Footer style="background-color: white">
                                    <Icon type="md-flame" />
                                    {{item.share_hot}}
                                    <Icon type="md-calendar" style="margin-left: 10px;" />
                                    {{item.share_date}}
                                </Footer>
                            </Layout>
                        </div>
                    </div>
                </a>
            </div>
        </TabPane>
    </Tabs>
</template>

<script>
    import httpaxios from "../../../unites/httpaxios";

    export default {
        name: "UserShare",
        data(){
            return{
                urlsdata:[]
            }
        },
        methods:{
            tourls(item){
                let url = this.$store.state.serviceurl+'/AddShareHot/'
                let postdata = {
                    id:item.id
                }
                httpaxios.post(this,url,postdata,response=>{})
                window.open(item.href,'_blank')
            },
            ontabs(name){
                switch (name) {
                    case "1":{
                        let url = this.$store.state.serviceurl+'/UserShareOrderHot/'
                        httpaxios.get(this,url,response=>{
                            this.urlsdata = response.data.data
                        })
                    }break
                    case "2":{
                        let url = this.$store.state.serviceurl+'/UserShareOrderDate/'
                        httpaxios.get(this,url,response=>{
                            this.urlsdata = response.data.data
                        })
                    }break
                }
            }
        },
        mounted() {
            let url = this.$store.state.serviceurl+'/UserShareOrderHot/'
            httpaxios.get(this,url,response=>{
                this.urlsdata = response.data.data
            })
        }
    }
</script>

<style scoped>
    .urls{
        width: 400px;
        height: 200px;
        background-color: white;
        border: 1px solid darkgray;
        border-radius: 10px;
        display: flex;
        overflow: hidden;
    }
    .urls:hover{
        box-shadow: 1px 1px 3px darkgray;
    }
</style>