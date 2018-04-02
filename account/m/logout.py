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

def web(req):
    if (req.session['username']):
        h = u"%s，您已经注销" % req.session['username']
        del req.session['username']
    else:
        h = "您已经注销"
    return HttpResponse(h)


def api(req):
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
                return JsonResponse({'code':200, 'msg':u'登录成功', 'result':''})
            else:
                return JsonResponse({'code':201, 'msg':u'账号或密码错误', 'result':[]})#HttpResponse(h)
        else:
            JsonResponse({'code': 204, 'msg': u'非法提交', 'result': ''})

    else:
        form = AddForm()

    content = {}
    content['system_name'] = 'GoFree'
    content['form'] = form
    #return render(req, 'login.html', content)
    #return HttpResponseNotFound()
    return HttpResponse(status=403)
