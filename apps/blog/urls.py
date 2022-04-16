from django.conf.urls import url
from django.urls import path
from blog.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^page/(\d+)$', IndexView.as_view()),
    url(r'^article/(\d+)$', DetailView.as_view()),
    url(r'^category/(\d+)$', getArticleByCid),
    url(r'^archive/(?P<year>\d+)/(?P<month>\d+)$', getArticleByAddtime),
    url(r'^archive/$', getArticleByAddtime),
]