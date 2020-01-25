from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UrlsClass(models.Model):
    classname = models.CharField(max_length=20,verbose_name='分类名')
    sortid = models.IntegerField(verbose_name='排序比重', default=5)
    def __str__(self):
        return self.classname
    def __unicode__(self):
        return self.classname
    class Meta:
        verbose_name = "公共资源分类"
        verbose_name_plural = "公共资源分类数据库"

class Urls(models.Model):
    title = models.CharField(max_length=30,verbose_name='标题')
    subtitle = models.CharField(max_length=100,verbose_name='描述')
    href = models.TextField(verbose_name='链接')
    image = models.ImageField(upload_to='image',verbose_name='图像')
    href_class = models.ForeignKey("UrlsClass",on_delete=models.CASCADE,verbose_name='所属分类')
    date = models.DateField(auto_now_add=True,verbose_name='录入时间')
    source = models.TextField(verbose_name='来源',default='hlzurlbavigation')
    sortid = models.IntegerField(verbose_name='排序比重',default=5)
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = "公共资源"
        verbose_name_plural = "公共资源数据库"

class PrivateResourcesClass(models.Model):
    classname = models.CharField(max_length=20, verbose_name='分类名')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='所属用户')
    date = models.DateField(auto_now_add=True,verbose_name='创建时间')
    def __str__(self):
        return self.classname
    def __unicode__(self):
        return self.classname
    class Meta:
        verbose_name = "私人资源分类"
        verbose_name_plural = "私人资源分类数据库"

class PrivateResources(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    subtitle = models.CharField(max_length=100, verbose_name='描述')
    href = models.TextField(verbose_name='链接')
    image = models.ImageField(upload_to='image', verbose_name='图像')
    href_class = models.ForeignKey("PrivateResourcesClass", on_delete=models.CASCADE,verbose_name='所属分类')
    date = models.DateField(auto_now_add=True, verbose_name='录入时间')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='所属用户')
    share = models.BooleanField(default=False,verbose_name='是否分享')
    share_date = models.DateField(auto_now_add=True,verbose_name='分享日期')
    share_hot = models.BigIntegerField(default=0,verbose_name='分享热度')
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = "私人资源"
        verbose_name_plural = "私人资源数据库"

class About(models.Model):
    content = models.TextField(verbose_name='文章内容')
    date = models.DateField(auto_now=True,verbose_name='发布时间')
    def __str__(self):
        return str(self.date)
    def __unicode__(self):
        return str(self.date)
    class Meta:
        verbose_name = "关于本站"
        verbose_name_plural = "关于本站数据库"

class WeChat(models.Model):
    image = models.ImageField(upload_to='wechat',verbose_name='二维码')
    class Meta:
        verbose_name = "微信二维码"
        verbose_name_plural = "微信二维码数据库"

class Comments(models.Model):
    content = models.TextField(verbose_name='评论内容')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='评论用户')
    date = models.DateField(auto_now_add=True,verbose_name='评论时间')
    def __str__(self):
        return self.content
    def __unicode__(self):
        return self.content
    class Meta:
        verbose_name = "用户评论"
        verbose_name_plural = "用户评论数据库"