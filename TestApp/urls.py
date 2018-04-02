# coding:utf-8
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views,testdb
from . import search
urlpatterns = [
    url(r'^/testdb$', testdb.testdb),
    url(r'^/search-form$',search.search_form),
    url(r'^/getInfo$',search.getInfo),
    url(r'^/loginMy$',views.loginMy,name='loginMy'),
    #url(r'^/search$', search.search),
    url(r'^/myApi$', views.myApi, name='myApi'),
    url(r'^/param/(?P<user_id>[0-9]+)/$', views.paramApi, name='paramApi'),
]
