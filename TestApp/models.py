# coding:utf-8
from django.db import models

# Create your models here.

class Luo(models.Model):
	name = models.CharField(max_length=20)
	phone = models.CharField(max_length=30, verbose_name=u"手机", null=False, default="")
	def __str__(self):
        	return self.name
