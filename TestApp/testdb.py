# -*- coding: utf-8 -*-
 
from django.http import HttpResponse

from TestApp.models import Luo

def testdb(request):
	test1 = Luo(name='你好啊')
	test1.save()
	return HttpResponse("<p>Data adding successful!</p>")
