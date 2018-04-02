# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .forms import AddForm
from .models import Luo

from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.contrib.auth.hashers import make_password, check_password
from .serializers import LuoSerializer

# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

def getInfo(req):
	if req.method == 'POST':
		form = AddForm(req.POST)
		if form.is_valid():
			name = form.clean_data['name']
			res = Luo.objects.filter(name=name)
			if res.exists():
				req.session['name'] = name
				h = 'Yes bingo'
				return JsonResponse({'code':200, 'msg':u'登录成功', 'result':UserSerializer(res[0]).data})
			else:
				return JsonResponse({'code':201, 'msg':u'账号或密码错误', 'result':[]})#HttpResponse(h)
		
		else:
			JsonResponse({'code': 204, 'msg': u'非法提交', 'result': ''})
	else:
		form = AddForm()
	content = {}
    	content['system_name'] = 'GoFree'
    	content['form'] = form
    	return render(req, 'getInfo.html', content)
