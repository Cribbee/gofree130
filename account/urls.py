# coding:utf-8
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views
urlpatterns = [

    url(r'^/login$', views.login, name='login'),
    url(r'^/login/api$', views.loginApi, name='loginApi'),

    url(r'^/logout$', views.logout, name='logout'),
    url(r'^/logout/api$', csrf_exempt(views.logoutApi), name='logoutApi'),

    url(r'^/register$', views.register, name='register'),
    url(r'^/register/api$', csrf_exempt(views.registerApi), name='registerApi'),

    url(r'^/veri_sms/api$', views.veriSmsApi, name='veri_sms'),

    url(r'^/veri_email/api$', views.sentEmail, name='veri_emsil'),

    url(r'^/preference/api$', views.preference, name='preference'),

    url(r'^/lzhtest/api$', views.lzhadd, name='l_add'),

    url(r'^/test$', views.testAlgorithm, name='testAlgorithm'),

    url(r'^/api$', views.api, name='api'),

    #test from by zwx 2018-03-30 22:34:49for
    url(r'^/from$', views.fromTest, name='test'),

]
