# coding: utf-8

from .. import models
from .. import serializers
import logging

def get_hotel_by_view_id(view_id):
    """
        获取景点周边的酒店
        BuildDate:2018-01-07
        Version:0.1
        Date:2018-01-07
        History:
        Args: view_id景点的id
        Returns: hotel_list酒店列表
    """
    logger = logging.getLogger('django')
    view_info = models.View.objects.filter(id=view_id).values('id','lat','lng')  # 不存在或存在多个的时候会报错
    logger.debug('------in nearby')
    # logger.debug(view_info[0]['lat'])
    lng = view_info[0]['lng']
    lat = view_info[0]['lat']
    # lng = 120.17734400
    # lat = 30.24873300
    # sql = " select place_hotel.*,(abs(lng-120.17734400) + abs(lat-30.24873300)) as distance from place_hotel order by distance  asc limit 10;  "
    sql = " select place_hotel.*,(abs(lng-%s) + abs(lat-%s)) as distance from place_hotel order by distance  asc limit 10;  " %(lng,lat)

    hotel_list = models.Hotel.objects.raw(sql)

    # view_info = View.objects.filter(id=view_id).values()  # 不存在或存在多个的时候会报错
    # logger.debug(view_info)
    # view_lng = view_info[0]['lng']
    # view_lat = view_info[0]['lat']
    # # 获取景点附近的餐饮信息
    # sql = " select place_eat.*,(abs(lng-%s) + abs(lat-%s)) as distance from place_eat order by distance  asc limit 10;  " % (
    # view_lng, view_lat)






    # for p in Hotel.objects.raw(sql):
    #    logger.debug('~~~~~~~~')
    #    logger.debug(p)
    serializer = serializers.HotelSerializer(hotel_list[0])
    #logger.debug(view_info)
    #logger.debug(view_info[0])
    return serializer.data


def get_eat_by_view_id(view_id):
    """
        获取景点周边的餐馆
        Author: luozonghai
        BuildDate:2017-12-31
        Version:0.1
        Date:2018-01-01
        History:
        Args:view_id 景点id
        Returns:eat_list 餐馆列表
    """
    logger = logging.getLogger('django')

    view_info = models.View.objects.filter(id=view_id).values('id','lng', 'lat')  #不存在或存在多个的时候会报错
    lng = view_info[0]['lng']
    lat = view_info[0]['lat']

    sql = " select place_eat.*,(abs(lng-%s) + abs(lat-%s)) as distance from place_eat order by distance  asc limit 10;  " % (
    lng, lat)
    eat_list = models.Eat.objects.raw(sql)

    eat_list_res = []
    for item in eat_list[0: 2]:
        serializer = serializers.EatSerializer(item)
        eat_list_res.append(serializer.data)
    #logger.debug(view_info)
    #logger.debug(view_info[0])
    return eat_list_res
