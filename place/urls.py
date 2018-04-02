# coding:utf-8
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    url(r'^/test_hotel/(?P<hotel_id>[0-9]+)/$', views.test_get_hotel, name='test_get_hotel'),
    url(r'^/getNearbyHotelByViewId/(?P<view_id>[0-9]+)/$', views.get_nearby_hotel_by_view_id, name='get'),
    url(r'^/getNearbyEatByViewId/(?P<view_id>[0-9]+)/$', views.get_nearby_eat_by_view_id, name='get'),
    url(r'^/getDailyRouting/(?P<view_id_list>[0-9]+)/$', views.get_daily_routing, name='get'),
]
