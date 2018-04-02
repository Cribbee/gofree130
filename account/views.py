# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django import http

#from .forms import AddForm
from . import forms
from account.models import Person
from .models import User
from .models import LzhTest

from .m import login as Login
from . import models

from django.contrib.auth.hashers import make_password, check_password

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt


def login(req):
	return Login.web(req)

@csrf_exempt
def loginApi(req):
    return Login.api(req)

def logout(req):
	try:
		h = u"%s，您已经注销" % req.session['username']
		del req.session['username']
	except KeyError:
		h = "您已经注销"
	return HttpResponse(h)

@csrf_exempt
def logoutApi(req):
	try:
		h = u"%s，您已经注销" % req.session['username']
		del req.session['username']
	except KeyError:
		h = "您已经注销"
		pass
	return JsonResponse({'code': 200, 'msg': h, 'result': []})

def preference(req):
	try:
		selectIds = req.session['selectIds']
	except KeyError:
		return JsonResponse({'code': 400, 'msg': u'插入失败', 'result': []})

	#return JsonResponse({'code': 401, 'msg': u'您未登录', 'result': []})
	#return JsonResponse({'code': 402, 'msg': u'用户不存在', 'result': []})

	return JsonResponse({'code': 200, 'msg': u'插入成功', 'result': []})

def register(req):
	if req.method == 'POST':
		form = forms.RegisterForm(req.POST)

		try:
			veri_code = req.session['veri_code']
			veri_code_datetime = req.session['veri_code_datetime']
		except KeyError:
			return HttpResponse(u'请先获取短信验证码')

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			confirm = form.cleaned_data['confirm']
			email = form.cleaned_data['email']
			phone = form.cleaned_data['phone']

			if (password != confirm):
				h = u"两次密码不一致"
				return HttpResponse(h)
			if models.User.objects.filter(username=username).exists():
				h = u"用户名已存在"
				return HttpResponse(h)
			else:
				p = models.User(username=username,
								password=make_password(password, None, 'pbkdf2_sha256'),
								email=email,
								phone=phone)
				p.save()
				h = u"注册成功"
			return http.HttpResponseRedirect('/account/login')

		else:
			return HttpResponse(u'非法提交')

	content = {}
	content['system_name'] = 'GoFree'
	content['form'] = forms.RegisterForm()
	return render(req, 'register.html', content)

@csrf_exempt
def fromTest(req):
	if req.method == 'POST':
		form = forms.RegisterForm(req.POST)
		if form.is_valid():
			return JsonResponse({'code': 400, 'msg': req.method, 'result': []})
		else:
			return render(req, 'register.html', {'form': form})
	else:
		form = forms.RegisterForm()
    	return render(req, 'register.html', {'form': form})

def registerApi(req):
	from .m import EmailSSL
	from .serializers import UserSerializer
	if req.method == 'POST':
		form = forms.RegisterForm(req.POST)

		try:
			veri_code = req.session['veri_code']
			veri_code_datetime = req.session['veri_code_datetime']
			veri_phone = req.session['veri_phone']
		except KeyError:
			return JsonResponse({'code': 201, 'msg': u'请先获取短信验证码', 'result': []})

		if form.is_valid():
			try:
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				confirm = form.cleaned_data['confirm']
				phone = form.cleaned_data['phone']
				code = form.cleaned_data['veri_code']
			except KeyError:
				return JsonResponse({'code': 202, 'msg': u'表单信息不完整', 'result': []})

			try:
				email = form.cleaned_data['email']
			except KeyError:
				email = ""
				pass

			if (password != confirm):
				return JsonResponse({'code': 203, 'msg': u'两次密码不一致', 'result': []})

			if (phone != veri_phone):
				pass # return JsonResponse({'code': 204, 'msg': u'该手机号码未经验证', 'result': []})

			if (veri_code != code):
				pass #return JsonResponse({'code': 205, 'msg': u'验证码错误', 'result': []})

			#if (veri_code_datetime)

			if models.User.objects.filter(username=username).exists():
				h = u"用户名已存在"
				return JsonResponse({'code': 206, 'msg': h, 'result': []})
			else:
				p = models.User(username=username,
								password=make_password(password, None, 'pbkdf2_sha256'),
								email=email,
								phone=phone)
				p.save()
				h = u"注册成功"
				EmailSSL.welecome(email, username)

			# 注册成功后自动登录
			try:
				username = form.cleaned_data['username']
				res = User.objects.filter(username=username)
			except KeyError:
				try:
					phone = form.cleaned_data['phone']
					res = User.objects.filter(phone=phone)
				except KeyError:
					return JsonResponse({'code': 600, 'msg': u'后端错误，请联系后端', 'result': []})  # HttpResponse(h)
			if res.exists() and check_password(password, res[0].password):
				# 注册成功后自动登录
				req.session['username'] = res[0].username
				return JsonResponse({'code': 200, 'msg': h, 'result': UserSerializer(res[0]).data})
			else:
				return JsonResponse({'code': 412, 'msg': u'账号或密码错误', 'result': []})  # HttpResponse(h)
		else:
			return JsonResponse({'code': 207, 'msg': u'非法提交', 'result': []})

	content = {}
	content['system_name'] = 'GoFree'
	content['form'] = forms.RegisterForm()
	return render(req, 'register.html', content)

@csrf_exempt
def veriSmsApi(req):
	from .m import SMS
	import random
	import time
	phone = req.GET['phone']
	veri_code = random.randint(1000, 10000)
	req.session['veri_code'] = "%4d" % veri_code
	req.session['veri_code_datetime'] = time.strftime('%Y%algorithm%d%H%M%S')
	req.session['veri_phone'] = phone
	return JsonResponse({'code':200, 'msg':SMS.verification(phone, veri_code), 'result':[]})

def sentEmail(req):
	from .m import EmailSSL
	EmailSSL.welecome("zouwx2cs@foxmail.com", "zouwx")
	return JsonResponse({'code': 200, 'msg': "邮件发送成功", 'result': []})

# @csrf_exempt
def api(req):
	from .serializers import UserSerializer
	from rest_framework.renderers import JSONRenderer
	from rest_framework.parsers import JSONParser

	res = User.objects.all()
	serializer = UserSerializer(res, many=True)
	return JsonResponse({'code': 200, 'msg': len(res), 'result': serializer.data}, safe=False)

def testAlgorithm(req):
	from persona.algorithm import rec
	res = rec.run()
	print "__file__=%s" % __file__
	return HttpResponse(res)


def lzhadd(request):
    from .serializers import LzhTestSerializer
    from rest_framework.renderers import JSONRenderer
    from rest_framework.parsers import JSONParser
    from .models import LzhTest

    #res = LzhTest.objects.all()
    #serializer = LzhTestSerializer(res, many=True)
    # LzhTest.objects.create(username="xixi",age=20)
    # LzhTest.objects.create(**{"username": "xiaoxi","age":19})
 
    # save方式一
    #au = Author(name="yj",age=20)
    #au.save()
 
    #save方式二
    thor = LzhTest()
    thor.username="lx"
    thor.password="21"
    #serializer.is_valid()
    thor.save()
 
    return HttpResponse("表记录添加成功")
 
