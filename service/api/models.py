from django.db import models

# Create your models here.
class UrlsClass(models.Model):
    classname = models.CharField(max_length=20,verbose_name='分类名')
    def __str__(self):
        return self.classname
    def __unicode__(self):
        return self.classname
    class Meta:
        verbose_name = "网址分类"
        verbose_name_plural = "网址分类数据库"

class Urls(models.Model):
    title = models.CharField(max_length=30,verbose_name='标题')
    subtitle = models.CharField(max_length=100,verbose_name='描述')
    href = models.TextField(verbose_name='链接')
    image = models.ImageField(upload_to='image',verbose_name='图像')
    href_class = models.ForeignKey("UrlsClass",on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True,verbose_name='录入时间')
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = "网址"
        verbose_name_plural = "网址数据库"