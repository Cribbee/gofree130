# coding:utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/getFirstPreference$', views.getFirstPreference),

    url(r'^/getCandidatePlaces/(?P<city_id>[0-9]+)/$', views.getCandidatePlaces),
    url(r'^/setLikePlaces$', views.setLikePlaces),
    url(r'^/recommendSchedule/(?P<city_id>[0-9]+)/start/(?P<start_date>[0-9]+)/end/(?P<end_date>[0-9]+)/$', views.recommendSchedule),
]
