<template>
    <Layout class="ResourcesManage">
        <Header style="background-color: white;display: flex;margin-bottom: 3px;">
            <h3>HLZUrlNavigation用户资源管理中心</h3>
            <div style="flex: 1;height: 100%;display: flex;flex-direction: row-reverse">
                <h3>用户：{{getuser()}}</h3>
            </div>
        </Header>
        <Content>
            <Layout style="width: 100%;height: 100%;">
                <Sider style="background-color: white;margin-right: 3px;">
                    <Menu style="width:100%;text-align: center" @on-select="onmenu" active-name="1">
                        <MenuItem name="1">
                            <Icon type="logo-buffer" />
                            资源总览
                        </MenuItem>
                        <MenuItem name="2">
                            <Icon type="md-add" />
                            增加资源
                        </MenuItem>
                        <MenuItem name="3">
                            <Icon type="md-brush" />
                            修改资源
                        </MenuItem>
                        <MenuItem name="4">
                            <Icon type="md-trash" />
                            删除资源
                        </MenuItem>
                    </Menu>
                </Sider>
                <Content>
                    <router-view></router-view>
                </Content>
            </Layout>
        </Content>
    </Layout>
</template>

<script>
    export default {
        name: "ResourcesManage",
        methods:{
            onmenu(name){
                switch (name) {
                    case "1":{
                        this.$router.replace({name:'ResourcesManage-pc'})
                    }break
                    case "2":{
                        this.$router.replace({name:'ResourcesManageAddView-pc'})
                    }break
                    case "3":{
                        this.$router.replace({name:'ResourcesManageUpdateView-pc'})
                    }break
                    case "4":{
                        this.$router.replace({name:'ResourcesManageDeleteView-pc'})
                    }break
                }
            },
            getuser(){
                return localStorage.getItem('user')
            }
        }
    }
</script>

<style scoped>
    .ResourcesManage{
        width: 100%;
        height: 100%;
        position: absolute;
    }
    .ivu-menu{
        position: unset;
    }
</style>