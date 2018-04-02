"""gofree130 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# coding: utf-8


from django.conf.urls import include, url
from django.contrib import admin

from blog.urls import router as blog_router
from account import urls as account
from TestApp import urls as TestApp
from persona import urls as persona
from place import urls as place

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account', include(account)),
    url(r'^TestApp', include(TestApp)),
    #include blog.urls
    url(r'^api/', include(blog_router.urls)),
    url(r'^persona', include(persona)),
    url(r'^place', include(place)),
]
