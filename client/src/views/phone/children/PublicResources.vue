<template>
    <div class="PublicResources">
        <van-sidebar v-model="activeKey" style="overflow: auto;max-height: 85vh" @change="onsidebar">
            <van-sidebar-item :title="item.classname" v-for="(item,index) in classdata" :key="index" />
        </van-sidebar>
        <div style="height: 100%;flex: 1">
            <div v-if="activeKey==-1" style="width: 100%;height: 100%;display:flex;flex-direction: column;align-items: center;justify-content: center;">
                <img src="../../../assets/bd-2.png" style="width: 80%;height: auto;">
                <h4 style="margin: 30px;">欢迎来到公共资源库，这里是官方提供的资源</h4>
            </div>
            <div v-else style="width: 100%;height: 100%;display: flex;flex-direction: column;align-items: center;overflow: auto;max-height: 85vh">
                <a style="margin: 10px;width: 90%;height: 100px;" v-for="(item,index) in urlsdata" :key="index" :href="item.href" target="_blank">
                    <div style="border: 1px solid darkgray;border-radius: 5px;box-shadow: 1px 1px 1px darkgray;width: 100%;height: 100%;display: flex;">
                        <div style="height: 100%;flex: 1;display: flex;align-items: center;justify-content: center;">
                            <img :src="$store.state.serviceurl+'/'+item.image" style="width: 80%;height: auto;border-radius: 50%">
                        </div>
                        <div style="height: 100%;flex: 2;display: flex;flex-direction: column;align-items: center;justify-content: center;overflow: auto;max-height: 20vh;padding-left: 10px;padding-right: 10px;">
                            <h4>{{item.title}}</h4>
                            <h5>{{item.subtitle}}</h5>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
    import httpaxios from "../../../unites/httpaxios";

    export default {
        name: "PublicResources",
        data(){
            return{
                activeKey:-1,
                classdata:[],
                urlsdata:[]
            }
        },
        methods:{
            onsidebar(index){
                let url = this.$store.state.serviceurl+'/urls/'
                let postdata = {
                    class_id:this.classdata[index].id
                }
                httpaxios.post(this,url,postdata,response=>{
                    this.urlsdata = response.data.data
                })
            }
        },
        mounted() {
            let url = this.$store.state.serviceurl+'/index/'
            httpaxios.get(this,url,response=>{
                this.classdata = response.data.data
            })
        }
    }
</script>

<style scoped>
    .PublicResources{
        width: 100%;
        height: 100%;
        display: flex;
    }
</style>