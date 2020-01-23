from django.urls import path
from . import views as api

urlpatterns = [
    path('index/',api.index),
    path('urls/',api.urls),
    path('image/<file>/',api.image),
    path('login/',api.userlogin),
    path('logout/',api.userlogout),
    path('resign/',api.userresign),
    path('updatepassword/',api.updatepassword),
    path('modifypassword/',api.modifypassword),
    path('privateresourcesclass/',api.privateresourcesclass),
    path('privateresources/',api.privateresources),
    path('changeshare/',api.changeshare),
    path('ResourcesManageOverView/',api.ResourcesManageOverView),
    path('AddPrivateResourcesClass/',api.AddPrivateResourcesClass),
    path('AddPrivateResources/',api.AddPrivateResources),
    path('UpdatePrivateResourcesClass/',api.UpdatePrivateResourcesClass),
    path('geturlsdata/',api.geturlsdata),
    path('UpdatePrivateResources/',api.UpdatePrivateResources),
    path('DeletePrivateResourcesClass/',api.DeletePrivateResourcesClass),
    path('DeletePrivateResources/',api.DeletePrivateResources),
    path('UserShareOrderHot/',api.UserShareOrderHot),
    path('UserShareOrderDate/',api.UserShareOrderDate),
    path('AddShareHot/',api.AddShareHot),
    path('IsSuperUser/',api.IsSuperUser),
    path('ReadAbout/',api.ReadAbout),
    path('UpdateAbout/',api.UpdateAbout),
    path('WeChatImage/',api.WeChatImage)
]