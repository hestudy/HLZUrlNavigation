<template>
    <div class="UserShare">
        <van-tabs type="card" animated swipeable @change="changetabs">
            <van-tab title="热度排序">
                <div style="height: 100%;height: 80vh;max-height: 80vh;overflow: auto;display: flex;flex-direction: column;align-items: center;">
                    <a style="margin: 10px;width: 90%;height: 100px;" v-for="(item,index) in urlsdata" :key="index" :href="item.href" target="_blank" @click="tourls(item)">
                        <div style="width: 100%;height: 100%;border: 1px solid darkgray;border-radius: 5px;box-shadow: 1px 1px 1px darkgray;display: flex;overflow: hidden;">
                            <div style="height: 100%;flex: 1;display: flex;align-items: center;justify-content: center;">
                                <img :src="$store.state.serviceurl+'/'+item.image" style="width: 80%;height: auto;border-radius: 50%;">
                            </div>
                            <div style="height: 100%;flex: 2;display: flex;flex-direction: column;">
                                <div style="width: 100%;flex: 3;display: flex;flex-direction: column;align-items: center;justify-content: center;overflow: auto;max-height: 20vh;padding-left: 10px;padding-right: 10px;">
                                    <h4>{{item.title}}</h4>
                                    <h5>{{item.subtitle}}</h5>
                                </div>
                                <div style="width: 100%;flex: 1;display: flex;align-items: center;justify-content: center;">
                                    <van-icon name="fire-o" />
                                    <h5>{{item.share_hot}}</h5>
                                    <van-icon name="calender-o" style="margin-left: 10px"/>
                                    <h5>{{item.share_date}}</h5>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>
            </van-tab>
            <van-tab title="时间排序">
                <div style="height: 100%;height: 80vh;max-height: 80vh;overflow: auto;display: flex;flex-direction: column;align-items: center;">
                    <a style="margin: 10px;width: 90%;height: 100px;" v-for="(item,index) in urlsdata" :key="index" :href="item.href" target="_blank" @click="tourls(item)">
                        <div style="width: 100%;height: 100%;border: 1px solid darkgray;border-radius: 5px;box-shadow: 1px 1px 1px darkgray;display: flex;overflow: hidden;">
                            <div style="height: 100%;flex: 1;display: flex;align-items: center;justify-content: center;">
                                <img :src="$store.state.serviceurl+'/'+item.image" style="width: 80%;height: auto;border-radius: 50%;">
                            </div>
                            <div style="height: 100%;flex: 2;display: flex;flex-direction: column;">
                                <div style="width: 100%;flex: 3;display: flex;flex-direction: column;align-items: center;justify-content: center;overflow: auto;max-height: 20vh;padding-left: 10px;padding-right: 10px;">
                                    <h4>{{item.title}}</h4>
                                    <h5>{{item.subtitle}}</h5>
                                </div>
                                <div style="width: 100%;flex: 1;display: flex;align-items: center;justify-content: center;">
                                    <van-icon name="fire-o" />
                                    <h5>{{item.share_hot}}</h5>
                                    <van-icon name="calender-o" style="margin-left: 10px"/>
                                    <h5>{{item.share_date}}</h5>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>
            </van-tab>
        </van-tabs>
    </div>
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
            },
            changetabs(index){
                switch (index) {
                    case 0:{
                        console.log('test')
                        let url = this.$store.state.serviceurl+'/UserShareOrderHot/'
                        this.getdata(url)
                    }break
                    case 1:{
                        let url = this.$store.state.serviceurl+'/UserShareOrderDate/'
                        this.getdata(url)
                    }break
                }
            },
            getdata(url){
                httpaxios.get(this,url,response=>{
                    this.urlsdata = response.data.data
                })
            }
        },
        mounted() {
            let url = this.$store.state.serviceurl+'/UserShareOrderHot/'
            this.getdata(url)
        }
    }
</script>

<style scoped>
    .UserShare{
        width: 100%;
        height: 100%;
    }
</style>