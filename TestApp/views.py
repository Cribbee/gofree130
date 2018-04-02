# -*- coding: utf-8 -*-
# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django import http

from .forms import AddForm
from . import forms
from .models import Luo

from . import models

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from .serializers import LuoSerializer

import logging

def loginMy(req):
    if req.method == 'POST':
        form = AddForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            res = User.objects.filter(name=name)
            if res.exists() :
                req.session['name'] = name;
                h = "登录成功"
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
    return render(req, 'loginMy.html', content)
    #return HttpResponseNotFound()
    #return HttpResponse(status=403)

@csrf_exempt
def myApi(req):
    #return login.myApi(req)
    if req.method == 'POST':
 
        form = AddForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            res = Luo.objects.filter(name=name)
            if res.exists() :
                # 先明文，后密文
                req.session['name'] = name;
                h = "登录成功"
                return JsonResponse({'code':200, 'msg':u'你好啊 in IF', 'result':LuoSerializer(res[0]).data})
            else:
                return JsonResponse({'code':201, 'msg':u'你不好 in ELSE', 'result':[]})#HttpResponse(h)
        else:
            JsonResponse({'code': 204, 'msg': u'非法提交', 'result': ''})

    else:
        form = AddForm()
    content = {}
    content['system_name'] = 'GoFree'
    content['form'] = form
    return render(req, 'login.html', content)

@csrf_exempt
def paramApi(req,user_id):

    if req.method == 'GET':
        luo = Luo.objects.filter(id=user_id)
        serializer = LuoSerializer(luo)
        logger = logging.getLogger('django')
        logger.debug('This is an error msg')
        logger.debug('~~~~~~~~~')
        logger.debug(luo)
        return JsonResponse({'code':200, 'msg':u'你好啊 in IF', 'result':LuoSerializer(luo[0]).data})
