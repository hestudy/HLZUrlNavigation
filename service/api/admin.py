from django.contrib import admin
from .models import UrlsClass,Urls

# Register your models here.
@admin.register(UrlsClass)
class UrlsClassAdmin(admin.ModelAdmin):
    list_display = ['classname']

@admin.register(Urls)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ['image','title','subtitle','href','href_class','date']
    list_filter = ['href_class']
    search_fields = ['title','subtitle']
    list_per_page = 20