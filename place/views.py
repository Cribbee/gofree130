# -*- coding: utf-8 -*-
# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import http

from .models import View
from .models import Hotel
from .models import Eat

from . import models

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from .serializers import ViewSerializer
from .serializers import HotelSerializer
from .serializers import EatSerializer

import logging

def test_get_hotel(req,hotel_id):
    """
        测试 根据id获取酒店信息
        Author: luozonghai
        BuildDate:2017-12-31
        Version:0.1
        Date:2018-01-01
        History:
    """
    logger = logging.getLogger('django')
    if req.method == 'GET':
        res = Hotel.objects.filter(id=hotel_id)
        hotelInfo = Hotel.objects.filter(id=hotel_id).values()
        lng = hotelInfo[0]['lng']
        lat = hotelInfo[0]['lat']
        logger.debug(hotelInfo)
        logger.debug(lng)
        logger.debug(lat)
        serializer = HotelSerializer(res)
        return JsonResponse({'code':200, 'msg':u'', 'result':HotelSerializer(res[0]).data})

def get_nearby_hotel_by_view_id(req,view_id):
    """
        获取景点周边的酒店
        Author: luozonghai
        BuildDate:2017-12-31
        Version:0.1
        Date:2018-01-01
        History:
        Args: view_id景点的id
        Returns: hotel_list酒店列表

        2018-03-22完成情况及存在的问题：
            能够获取某个景点附近的酒店，10个，根据距离远近进行排序
            问题：分页未加，排序方式单一，后期可加入评分等进行权重考虑再排序
            sql可优化、索引等
    """
    logger = logging.getLogger('django')
    if req.method == 'GET':
        #获取景点的经纬度
        view_info = View.objects.filter(id=view_id).values()  #不存在或存在多个的时候会报错
        logger.debug(view_info)
        view_lng = view_info[0]['lng']
        view_lat = view_info[0]['lat']
        #获取景点附近的酒店
        sql = " select place_hotel.*,(abs(lng-%s) + abs(lat-%s)) as distance from place_hotel order by distance  asc limit 10;  " %(view_lng,view_lat)
        hotel_list = Hotel.objects.raw(sql)
        serializer = HotelSerializer(hotel_list)

        return JsonResponse({'code':200, 'msg':u'', 'result':HotelSerializer(hotel_list,many=True).data})


def get_nearby_eat_by_view_id(req,view_id):
    """
        获取景点周边的餐馆
        Author: luozonghai
        BuildDate:2017-12-31
        Version:0.1
        Date:2018-01-01
        History:
        Args:view_id 景点id
        Returns:eat_list 餐馆列表

        2018-03-22完成情况及存在的问题：
            能够获取某个景点附近的餐厅，10个，根据距离远近进行排序
            问题：分页未加，排序方式单一，后期可加入评分等进行权重考虑再排序
            sql可优化、索引等
    """
    logger = logging.getLogger('django')
    if req.method == 'GET':
        #获取景点的经纬度
        view_info = View.objects.filter(id=view_id).values()  #不存在或存在多个的时候会报错
        logger.debug(view_info)
        view_lng = view_info[0]['lng']
        view_lat = view_info[0]['lat']
        #获取景点附近的餐饮信息
        sql = " select place_eat.*,(abs(lng-%s) + abs(lat-%s)) as distance from place_eat order by distance  asc limit 10;  " %(view_lng,view_lat)
        eat_list = Eat.objects.raw(sql)
        serializer = EatSerializer(eat_list)

        return JsonResponse({'code':200, 'msg':u'', 'result':EatSerializer(eat_list,many=True).data})

#def  get_daily_routing(req,day_num,view_id_list):  #完整的格式
def  get_daily_routing(req,view_id_list):#暂时用这个
    """
    功能:根据传入的旅游天数（如3天）和景点id列表（如20个），获取每日景点列表（每日3个，共9个）
    参数：day_num游玩天数，view_id_list景点列表     目前先写死，功能完成后再出来参数，配置url
    返回：列表
         result:
               0:第一天
                 view_list:景点列表，3个  view1 view 2 view3
                 hotel_list:酒店列表，根据view3找附近，hotel1,hotel2...hoteln
                 eat_list:餐厅列表
                     lunch:午餐列表 ，根据view2找附近,eat1,eat2...eatn
                     supper:晚餐列表，根据view3找附近,eat1,eat2...eatn
               1:第二天
                 view_list...
                 ...

                即，午餐以每天的第二个景点为中心，查找附近的餐厅
                    晚餐以每天的第三个景点为中心，查找附近的餐厅
                    酒店以第二天的第一个景点为中心，
                
    其他：目前每日三个景点：上午1个下午2个，默认每个1.5h，
          建议：可先选出前3*day_num个景点，只按照评分高低选择
                然后分为day_num部分，对每一部分再选景点和餐馆 
             
           熟悉以后再按照 60%评分+40%距离进行选择,因为sql有点麻烦，直接Django写不好写:
             ORDER BY ( 
                        0.6 * pts + 
                        0.4 * 1/abs(lng - lng0)+ 1/abs(lat - lat0)  #经纬度差距越小越接近，则排名应越高，故 1/xx
                      ) DESC LIMIT xx
    """
    from django.forms.models import model_to_dict
    import json
    from .m import nearby
    logger = logging.getLogger('django')
    if req.method == 'GET':
        #10个里面选出5个分最高的
        view_id_list = ['11','13','15','17','19','21','24','26','28','30','31','33'] 
        id_in_sql = ",".join(view_id_list)
        day_view = []
        view_set = View.objects.filter(id__in=view_id_list).values('id').order_by('-pts')[:9]
        logger.debug(view_set)
        """
          03-24完成情况及还需改善的问题
                已完成基本情况
                排序需要加上权重
                还需加上分页功能
          
        """

        #景点排序
        # 11,28,26,
        # 24,21,19,
        # 17,15,13

        # 即，午餐以每天的第二个景点为中心，查找附近的餐厅
        # 晚餐以每天的第三个景点为中心，查找附近的餐厅
        # 酒店以第二天的第一个景点为中心，  ---->暂时以第三个景点为中心查找当日酒店

        days_view = [] #每天的景点
        center = {}
        #景点分组
        for i in range(0, (len(view_set)+1)//3):
            if i == (len(view_set)+1)//3: # if i == 3   10//3 =3 整数部分
                day_view = view_set[i*3: -1]
            else:# all in else
                day_view = view_set[i*3: i*3+3]
                logger.debug('++++++++++++++++ 第 %s 天+++++++++++++++++++++++'%(i+1))
                logger.debug('---view')
                logger.debug(view_set[i*3: i*3+3])
                # i*3+0第一个景点 i*3+1第二个景点 i*3+2第三个景点
                center['hotel'] = view_set[i*3+2] #景点中心：第三个景点
                center['lunch'] = view_set[i*3+1] #午餐以第二个为中心
                center['supper'] = view_set[i*3+2]#晚餐以第三个为中心
                logger.debug('---center')
                logger.debug(center)
            eat_list = {}
            eat_list['luch'] = nearby.get_eat_by_view_id(center['lunch']['id']) #获取午餐饭店列表
            eat_list['supper'] = nearby.get_eat_by_view_id(center['supper']['id'])#获取晚餐饭店列表
            days_view.append({"day": i+1, "view": ViewSerializer(day_view, many=True).data, "hotel": nearby.get_hotel_by_view_id(center['hotel']['id']), "eat":eat_list})
        #serializer =
        #res = serializer.data

        #day_view.append("abc")
        return JsonResponse({'code': 200, 'msg': len(view_set), 'result': days_view}, safe=False)


