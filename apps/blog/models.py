from datetime import datetime

from django.db import models

from mdeditor.fields import MDTextField


# Create your models here.
class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True


class Category(BaseModel):
    """文章分类"""
    name = models.CharField('分类名', max_length=30, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = "分类"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name
    

class Tag(BaseModel):
    """文章标签"""
    name = models.CharField('标签名', max_length=30, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = "标签"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name

class Article(BaseModel):
    """文章"""
    title = models.CharField(max_length=200,unique=True,verbose_name='标题')
    desc = models.CharField(max_length=200,verbose_name='简介', blank=True)
    content = MDTextField(verbose_name='内容')
    category = models.ForeignKey(Category,verbose_name='所属类别',on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField(Tag,verbose_name='所属标签', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

