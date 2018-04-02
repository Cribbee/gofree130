# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseForbidden
from django import http

from ..forms import AddForm
from ..models import Person
from ..models import User


from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.contrib.auth.hashers import make_password, check_password
from ..serializers import UserSerializer

def web(req):
    if req.method == 'POST':
        form = AddForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            res = User.objects.filter(username=username)
            if res.exists() and check_password(password, res[0].password):
                # 先明文，后密文
                req.session['username'] = username
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

def api(req):
    if req.method == 'POST':
        try:
            password = req.POST['password']
        except KeyError:
            return JsonResponse({'code': 410, 'msg': u'缺少密码参数', 'result': []})  # HttpResponse(h)

        try:
            username = req.POST['username']
            res = User.objects.filter(username=username)
        except KeyError:
            try:
                phone = req.POST['phone']
                res = User.objects.filter(phone=phone)
            except KeyError:
                return JsonResponse({'code': 411, 'msg': u'需要账号或手机号', 'result': []})  # HttpResponse(h)

        if res.exists() and check_password(password, res[0].password):
            # 先明文，后密文
            req.session['username'] = res[0].username
            return JsonResponse({'code':200, 'msg':u'登录成功', 'result':UserSerializer(res[0]).data})
        else:
            return JsonResponse({'code':412, 'msg':u'账号或密码错误', 'result':[]})#HttpResponse(h)

    else:
        form = AddForm()

        content = {}
        content['system_name'] = 'GoFree'
        content['form'] = form
        return render(req, 'login.html', content)
        #return HttpResponseNotFound()
        #return HttpResponse(status=403)

