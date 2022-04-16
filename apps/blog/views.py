import math

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator  
from django.core.paginator import Paginator
from django.views.generic import View 
from django.db.models import Count

from blog.models import *


# Create your views here.
class IndexView(View):

    def get(self,request,num=1):
        num = int(num)

        #查询数据库中所有的贴子信息
        ArticleList = Article.objects.all().order_by('add_time')
        #创建分页器对象
        page_obj = Paginator(ArticleList,3) # 每页显示3条文章
        #获取某一页数据
        page_article = page_obj.page(num)

        #获取每一页显示页码数列表[2,...,11]
        begin = num - int(math.ceil(10.0/2))
        if begin <1:
            begin =1
        end = begin + 9
        if end > page_obj.num_pages:
            end = page_obj.num_pages

        if end <10:
            begin = 1
        else:
            begin = end -9

        page_list = range(begin,end+1)

        return render(request,'index.html',{'ArticleList':page_article,'page_list':page_list,'CurrentNum':num})

class DetailView(View):
    # 文章详情
    def get(self,request,article_id):
        article_id = int(article_id)

        article_obj = Article.objects.get(id=article_id)

        return render(request,'detail.html',{'article_obj':article_obj})


def getArticleByCid(request,category_id):
    category_id = int(category_id)

    c_article = Article.objects.filter(category_id=category_id)

    return render(request,'article-list.html',{'c_article':c_article})

def getArticleByAddtime(request,year=1,month=1):
    year = int(year)
    month = int(month)

    if year==1 and month==1:
        c_article = Article.objects.all().order_by('add_time')
    else:
        c_article = Article.objects.filter(add_time__year=year,add_time__month=month)

    return render(request,'article-list.html',{'c_article':c_article})

def getSidebarInfo(request):
    # 分类
    r_cate_article = Article.objects.values('category__name','category').annotate(c=Count('*')).order_by('c')
    # 外键关联查询用双下划线"__"

    # 按时间归档
    articles = Article.objects.all()
    year_month = set()   
    for a in articles:
        year_month.add((a.add_time.year,a.add_time.month))  #把每篇文章的年、月以元组形式添加到集合中
    counter = {}.fromkeys(year_month,0)  #以元组作为key，初始化字典
    for a in articles:
        counter[(a.add_time.year,a.add_time.month)]+=1  # 按年月统计文章数目
    year_month_number = []  #初始化列表
    for key in counter:
        year_month_number.append([key[0],key[1],counter[key]])  # 把字典转化为（年，月，数目）元组为元素的列表
    year_month_number.sort(reverse=True)  # 排序
    r_file_article =year_month_number

    # 近期文章
    r_recent_article = Article.objects.all().order_by('add_time')

    return {'r_cate_article':r_cate_article,'r_file_article':r_file_article,'r_recent_article':r_recent_article}