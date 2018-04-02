#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Scenic
from .serializers import ScenicSerializer
import logging



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



@csrf_exempt
def getFirstPreference(request):
    """
    列出所有的实例，或创建一个新的实例.
    """
    if request.method == 'GET':
        #scenic = Scenic.objects.all()
        #serializer = ScenicSerializer(scenic, many=True)
        #return JSONResponse(scenic)
        return HttpResponse(request.body)

    elif request.method == 'POST':
        #import json
        from . import math
        #data = JSONParser().parse(request)
        #req = json.loads(request.body)
        #serializer = ScenicSerializer(data=data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return JSONResponse(serializer.data, status=200)

        #print(request.body)
        #req = json.loads(request.body)

        #return HttpResponse(math.add(req['scenicId']))
        return HttpResponse(request.body)

@csrf_exempt
def getCandidatePlaces(req, city_id):
    from place.models import View
    from place.serializers import ViewSerializer
    if req.method == 'GET':

        views = View.objects.filter(city_id=city_id).values("name").distinct()\
            .values("id", "name", "city_id", "cmt_num", "main_pic").order_by("-cmt_num")
        serializer = ViewSerializer(views, many=True)
        return JSONResponse({'code': 200, 'msg': len(views[:25]), 'result': views[:25]})#serializer.data)
    else:
        return JSONResponse({'code': 410, 'msg': u'请求非法', 'result': []}, safe=False)
'''
@csrf_exempt
def setLikePlaces(req):
    from .models import Scenic

    if req.method == 'POST':
        import json
        from . import math
        # data = JSONParser().parse(request)
        # req = json.loads(request.body)
        # serializer = ScenicSerializer(data=data)
        # if serializer.is_valid():
        #    serializer.save()
        #    return JSONResponse(serializer.data, status=200)

        print(req.body)
        json_data = json.loads(req.body)

        succList = []

        for item in json_data['view_ids']:
            try:
                scenic = Scenic(user_id = json_data['user_id'],
                                user_name = "",
                                #user_lv = 0,
                                view_id = item,
                                view_name = "",
                                city_id = 3301,
                                cmt_num = 0,
                                #created = models.DateTimeField(auto_now_add=True)
                                #updated = models.DateTimeField(auto_now=True)
                                pts = 5,
                                #TYPE_CHOICES = (('0','firstTime'),('1','recommend'),('2','feedBack'))
                                type = 0)
                scenic.save()
                succList.append(item)
            except:
                pass

        return JSONResponse({'code': 200, 'msg': u'全部设置成功', 'result': succList})  # serializer.data)
    else:
        return JSONResponse({'code': 410, 'msg': u'请求非法', 'result': []}, safe=False)
'''

@csrf_exempt
def setLikePlaces(req):
    from .models import Scenic

    if req.method == 'POST':
        import json
        from . import math
        # data = JSONParser().parse(request)
        # req = json.loads(request.body)
        # serializer = ScenicSerializer(data=data)
        # if serializer.is_valid():
        #    serializer.save()
        #    return JSONResponse(serializer.data, status=200)

        #print(req.body)
        #json_data = json.loads(req.body)

        succList = []

        for item in str(req.POST['view_ids']).split('@'):
            try:
                scenic = Scenic(user_id = req.POST['user_id'],
                                user_name = "",
                                #user_lv = 0,
                                view_id = item,
                                view_name = "",
                                city_id = 3301,
                                cmt_num = 0,
                                #created = models.DateTimeField(auto_now_add=True)
                                #updated = models.DateTimeField(auto_now=True)
                                pts = 5,
                                #TYPE_CHOICES = (('0','firstTime'),('1','recommend'),('2','feedBack'))
                                type = 0)
                scenic.save()
                succList.append(item)
            except:
                pass

        return JSONResponse({'code': 200, 'msg': u'全部设置成功', 'result': succList})  # serializer.data)
    else:
        return JSONResponse({'code': 410, 'msg': u'请求非法', 'result': []}, safe=False)

def recommendSchedule(req, city_id, start_date, end_date):
    import datetime
    from place.models import View
    from place.serializers import ViewSerializer
    from place.m import nearby
    start_date = int(start_date)
    end_date = int(end_date)
    start = datetime.datetime(start_date//10000, start_date%10000//100, start_date%100)
    end = datetime.datetime(end_date//10000, end_date%10000//100, end_date%100)

    days = (end - start).days
    #return HttpResponse(req.body)
    #return JSONResponse({'code': 410, 'msg': u'请求非法', 'result': []})

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
    # from .m import nearby
    logger = logging.getLogger('django')

    # 10个里面选出5个分最高的
    view_id_list = ['11', '13', '15', '17', '19', '21', '24', '26', '28', '30', '31', '33']
    id_in_sql = ",".join(view_id_list)
    day_view = []
    view_set = View.objects.filter(id__in=view_id_list).order_by('-pts')[:9]
    """
      按照选评分出前9个景点以后，需要分组，再查找餐馆和酒店....

    """

    days_view = []
    for i in range(0, (len(view_set) + 1) // 3):
        if i == (len(view_set) + 1) // 3:
            day_view = view_set[i * 3: -1]
        else:
            day_view = view_set[i * 3: i * 3 + 3]
        days_view.append({"day": i + 1, "view": ViewSerializer(day_view, many=True).data,
                          "hotel": nearby.get_hotel_by_view_id(1),
                          "eat": nearby.get_eat_by_view_id(1)})

    # serializer =
    # res = serializer.data

    # day_view.append("abc")
    return JsonResponse({'code': 200, 'msg': len(view_set), 'result': days_view})