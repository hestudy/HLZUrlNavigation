from django.contrib import admin
from .models import UrlsClass,Urls,PrivateResourcesClass,PrivateResources,About,WeChat,Comments

# Register your models here.
@admin.register(UrlsClass)
class UrlsClassAdmin(admin.ModelAdmin):
    list_display = ['classname','sortid']

@admin.register(Urls)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ['title','image','subtitle','href','href_class','source','sortid','date']
    list_filter = ['href_class']
    search_fields = ['title','subtitle']
    list_per_page = 20

@admin.register(PrivateResourcesClass)
class PrivateResourcesClassAdmin(admin.ModelAdmin):
    list_display = ['classname','user','date']
    list_filter = ['user']
    list_per_page = 20

@admin.register(PrivateResources)
class PrivateResourcesAdmin(admin.ModelAdmin):
    list_display = ['title','image','subtitle','href','href_class','user','date','share','share_date','share_hot']
    list_filter = ['user']
    search_fields = ['title', 'subtitle']
    list_per_page = 20

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['date']

@admin.register(WeChat)
class WeChatAdmin(admin.ModelAdmin):
    list_display = ['image']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['content','user','date']
    list_per_page = 20
    list_filter = ['user']
    search_fields = ['content']