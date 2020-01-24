# 一个基于Django+Vue的网址导航系统

## 使用此项目注意

**确保你熟悉Vue和Django，能自己进行二次开发，因为本人未做任何便于理解和使用的封装**

## 前端

**使用Vue开发，未自定义组件，每个界面皆是View，可自行进行二次开发**

### 目录结构

```powershell
│  App.vue
│  main.js
│  
├─assets #静态资源
│      bd-1.png
│      bd-2.png
│      bd-3.png
│      bd-4.png
│      bd-5.png
│      
├─router
│      index.js #路由
│      
├─store
│      index.js #Vuex
│      
├─unites
│      httpaxios.js #封装axios请求工具
│      
└─views
    │  Home.vue #判断跳转pc还是phone
    │  
    ├─pc
    │  │  EditContent.vue #编辑文章界面
    │  │  Home.vue #主界面
    │  │  ResourcesManage.vue #资源管理界面
    │  │  UpdatePassword.vue #修改密码界面
    │  │  
    │  └─children
    │          About.vue #关于界面
    │          Home.vue #子主页
    │          PrivateResources.vue #私人资源界面
    │          PublicResources.vue #公开资源界面
    │          ResourcesManageAddView.vue #增加资源界面
    │          ResourcesManageDeleteView.vue #删除资源界面
    │          ResourcesManageOverView.vue #资源总览界面
    │          ResourcesManageUpdateView.vue #修改资源界面
    │          UserShare.vue #用户分享资源界面
    │          
    └─phone
            Home.vue #待开发phone适配界面
```



## 后端

**使用Django开发**

### 目录结构

```powershell
│  manage.py #运行程序
│  
├─api
│  │  admin.py #admin界面
│  │  apps.py 
│  │  models.py #数据库设计
│  │  tests.py
│  │  urls.py #路由
│  │  views.py #后端逻辑
│  │  __init__.py
│  │  
│  ├─migrations #数据库更改文件
│  │  │  0001_initial.py
│  │  │  0002_urls_source.py
│  │  │  0003_urls_sortid.py
│  │  │  0004_urlsclass_sortid.py
│  │  │  0005_auto_20200121_2025.py
│  │  │  0006_auto_20200121_2026.py
│  │  │  0007_auto_20200121_2033.py
│  │  │  0008_auto_20200122_2036.py
│  │  │  0009_about.py
│  │  │  0010_wechat.py
│  │  │  0011_comments.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          0001_initial.cpython-37.pyc
│  │          0002_urls_source.cpython-37.pyc
│  │          0003_urls_sortid.cpython-37.pyc
│  │          0004_urlsclass_sortid.cpython-37.pyc
│  │          0005_auto_20200121_2025.cpython-37.pyc
│  │          0006_auto_20200121_2026.cpython-37.pyc
│  │          0007_auto_20200121_2033.cpython-37.pyc
│  │          0008_auto_20200122_2036.cpython-37.pyc
│  │          0009_about.cpython-37.pyc
│  │          0010_wechat.cpython-37.pyc
│  │          0011_comments.cpython-37.pyc
│  │          __init__.cpython-37.pyc
│  │          
│  └─__pycache__
│          admin.cpython-37.pyc
│          models.cpython-37.pyc
│          urls.cpython-37.pyc
│          views.cpython-37.pyc
│          __init__.cpython-37.pyc
│          
├─image #后端存储图像
│      135949.png
│      135949_EkSAuWw.png
│      135973.png
│      135973_MtHhAzE.png
│      135977.png
│      135982.png
│      Snipaste_2020-01-21_11-18-43.png
│      Snipaste_2020-01-21_11-18-43_0IuBOLi.png
│      Snipaste_2020-01-21_11-18-43_1TaKyn7.png
│      Snipaste_2020-01-21_11-18-43_5q3Lc2b.png
│      Snipaste_2020-01-21_11-18-43_BJvjrrT.png
│      Snipaste_2020-01-21_11-18-43_jaFvMEg.png
│      Snipaste_2020-01-21_11-18-43_TDUJQ9s.png
│      Snipaste_2020-01-21_11-18-43_VemOcjx.png
│      Snipaste_2020-01-21_11-18-43_ZfGcx01.png
│      
├─service
│  │  asgi.py
│  │  settings.py #配置文件
│  │  urls.py #根路由
│  │  wsgi.py
│  │  __init__.py
│  │  
│  └─__pycache__
│          settings.cpython-37.pyc
│          urls.cpython-37.pyc
│          wsgi.cpython-37.pyc
│          __init__.cpython-37.pyc
│          
└─wechat #微信二维码
        微信图片_20200124012613.jpg
```

### 关于部署

**更改setting.py**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
        'NAME': 'YouDataBase', #更改为你的数据库
        'PASSWORD': 'YouPassWord', #更改为你的数据库用户
        'HOST':'localhost', #更改为你的数据库密码
        'PORT':'3306',
    }
}
```

**安装依赖(测试环境为windows 10，若ubuntu，需要使用pip3，也可能需要安装额外依赖)**

```shell
pip install mysqlclient
pip install django-cors-headers
```

**生成数据库**

```shell
python manage.py makemigrations
python manage.py migrate
```

**创建管理员账户**

```shell
python manage.py createsuperuser
```

**运行后端服务**

```shell
python manage.py runserver 0.0.0.0:8000
```

**更改前端Vuex配置文件**

```javascript
export default new Vuex.Store({
  state: {
    serviceurl:'http://127.0.0.1:8000/api'
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
```

**运行vue项目即可**