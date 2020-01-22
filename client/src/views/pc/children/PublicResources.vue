<template>
    <Layout class="publicresources">
        <Sider style="background: white;margin-right: 3px;">
            <Menu style="width: 100%;overflow: auto;max-height: 85vh;text-align: center" ref="menu1" @on-select="onmenu">
                <MenuItem :name="item.id" v-for="(item,index) in classdata" :key="index">
                    {{item.classname}}
                </MenuItem>
            </Menu>
        </Sider>
        <Content>
            <div v-if="menuselect==0" style="width: 100%;height: 100%;display: flex;align-items: center;justify-content: center;">
                <img src="../../../assets/bd-2.png" style="width: 60%;height: 70%;">
                <h3 style="z-index: 999;position: absolute;">欢迎来到公共资源库，这里是官方提供的网址资源</h3>
            </div>
            <div v-else style="width: 100%;height: 100%;padding: 10px;display: flex;flex-wrap: wrap;overflow: auto;max-height: 85vh;align-content: flex-start;">
                <a style="margin: 10px;" v-for="(item,index) in urlsdata" :key="index" target="_blank" :href="item.href">
                    <div class="urls">
                        <div style="height: 100%;flex: 1;display: flex;align-items: center;justify-content: center;">
                            <img :src="getimagesrc(item)" style="width:100%;height:auto;border-radius: 50%;">
                        </div>
                        <div style="height: 90%;width: 1px;background: darkgray;"></div>
                        <div style="height: 100%;flex: 2;">
                            <Layout style="width: 100%;height: 100%;">
                                <Header style="background: white;">
                                    <h3>{{item.title}}</h3>
                                </Header>
                                <Content style="background: white;padding: 10px;">
                                    <h4>{{item.subtitle}}</h4>
                                </Content>
                                <Footer style="background: white;">
                                    <h5>来源：{{item.source}}</h5>
                                </Footer>
                            </Layout>
                        </div>
                    </div>
                </a>
            </div>
        </Content>
    </Layout>
</template>

<script>
    import httpaxios from "../../../unites/httpaxios";
    export default {
        name: "PublicResources",
        data(){
            return{
                classdata:[],
                menuselect:0,
                urlsdata:[]
            }
        },
        mounted() {
            let url = this.$store.state.serviceurl+'/index'
            httpaxios.get(this,url,response=>{
                this.classdata = response.data.data
            })
        },
        methods:{
            onmenu(name){
                this.menuselect = name
                let url = this.$store.state.serviceurl+'/urls/'
                let postdata = {
                    class_id:name
                }
                httpaxios.post(this,url,postdata,response=>{
                    this.urlsdata = response.data.data
                })
            },
            getimagesrc(item){
                return this.$store.state.serviceurl+'/'+item.image
            }
        }
    }
</script>

<style scoped>
    .publicresources{
        width: 100%;
        height: 100%;
    }
    .ivu-menu{
        position: unset;
    }
    .urls{
        width: 400px;
        height: 200px;
        border-radius: 5px;
        padding: 10px;
        background: white;
        display: flex;
        align-items: center;
    }
    .urls:hover{
        box-shadow: 1px 1px 3px darkgray;
    }
</style>