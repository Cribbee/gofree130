# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseForbidden
from django import http

from ..forms import AddForm
from ..models import Luo


from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.contrib.auth.hashers import make_password, check_password
from ..serializers import LuoSerializer

def web(req):
    if req.method == 'POST':
        form = AddForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            res = User.objects.filter(username=username)
            if res.exists() and check_password(password, res[0].password):
                # 先明文，后密文
                req.session['username'] = username;
                h = "登录成功"
                return http.HttpResponseRedirect('/home')
            else:
                h = "账号或密码错误"

            return HttpResponse(h)
        else:
            return HttpResponse(u'非法提交')

    else:
        form = AddForm()

    content = {}
    content['system_name'] = 'GoFree'
    content['form'] = form
    return render(req, 'login.html', content)

def myApi(req):

    if req.method == 'POST':
        form = AddForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            phone = form.cleaned_data['phone']
            res = User.objects.filter(name=(name)
            if res.exists() :
                # 先明文，后密文
                req.session['name'] = name;
                h = "登录成功"
                return JsonResponse({'code':200, 'msg':u'登录成功', 'result':LuoSerializer(res[0]).data})
            else:
                return JsonResponse({'code':201, 'msg':u'账号或密码错误', 'result':[]})#HttpResponse(h)
        else:
            JsonResponse({'code': 204, 'msg': u'非法提交', 'result': ''})

    else:
        form = AddForm()

    content = {}
    content['system_name'] = 'GoFree'
    content['form'] = form
    return render(req, 'login.html', content)
    #return HttpResponseNotFound()
    #return HttpResponse(status=403)

