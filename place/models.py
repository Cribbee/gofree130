# coding:utf-8
from django.db import models

# Create your models here.


class View(models.Model):
    """
        景点信息
        Author: luozonghai
        BuildDate:2017-12-31
        Version:0.1
        Date:2017-12-31
        History:
    """
    country_id = models.IntegerField(verbose_name=u"所属国家id",default=-1)
    city_id = models.IntegerField(verbose_name=u"所属城市id",default=-1)
    name = models.CharField(max_length=200, verbose_name=u"景点名称",default="")
    addr = models.CharField(max_length=200, verbose_name=u"地址",default="")
    price = models.CharField(max_length=200, default="")
    lng = models.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    lat = models.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    cmt_num = models.IntegerField(verbose_name=u"评论数目",default=-1)
    pts = models.DecimalField(max_digits=16, verbose_name=u"评分",decimal_places=8,default=0.0)
    tel = models.CharField(max_length=200, verbose_name=u"联系电话",default="", null=True)
    time_cost = models.CharField(max_length=200, verbose_name=u"建议游览时间",default="", null=True)
    trans = models.TextField(verbose_name=u"交通路线",default="", null=True)
    open_time = models.CharField(max_length=200, verbose_name=u"开放时间",default="", null=True)
    main_pic = models.CharField(max_length=200, verbose_name=u"景点主图",default="")
    url = models.TextField(verbose_name=u"url链接",default="", null=True)
    status = models.IntegerField(verbose_name=u"景点状态",default=-1)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)

    # def __str__(self):
    #     #return self.name
    #     return self.tel
    #
    # def toJSON(self):
    #     fields = []
    #     for field in self._meta.fields:
    #         fields.append(field.name)
    #
    #     d = {}
    #     for attr in fields:
    #         d[attr] = getattr(self, attr)
    #
    #     import json
    #     return json.dumps(d)
    def __getitem__(self, k):
        return self.name



class Hotel(models.Model):
    """
        酒店信息
        Author: luozonghai
        BuildDate:2018-01-01
        Version:0.1
        Date:2018-01-01
        History:
    """
    country_id = models.IntegerField(verbose_name=u"所属国家id",default=-1)
    city_id = models.IntegerField(verbose_name=u"所属城市id",default=-1)
    name = models.CharField(max_length=200, verbose_name=u"酒店名称",default="")
    en_name = models.CharField(max_length=200, verbose_name=u"酒店英文名称",default="")
    addr = models.CharField(max_length=200, verbose_name=u"酒店地址",default="")
    price = models.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    lng = models.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    lat = models.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    cmt_num = models.IntegerField(verbose_name=u"评论数目",default=-1)
    pts = models.DecimalField(max_digits=16, verbose_name=u"评分",decimal_places=8,default=0.0)
    pts_level = models.CharField(max_length=200, verbose_name=u"评分等级",default="")
    note_num = models.IntegerField(verbose_name=u"游记数目",default=-1)
    desc = models.CharField(max_length=200, verbose_name=u"描述",default="")
    main_pic = models.CharField(max_length=200, verbose_name=u"酒店主图",default="")
    url = models.TextField( verbose_name=u"url链接",default="", null=True)
    status = models.IntegerField(verbose_name=u"酒店状态",default=-1)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name




class Eat(models.Model):
    """
        餐厅信息
        Author: luozonghai
        BuildDate:2018-01-01
        Version:0.1
        Date:2018-01-01
        History:
    """
    country_id = models.IntegerField(verbose_name=u"所属国家id",default=-1)
    city_id = models.IntegerField(verbose_name=u"所属城市id",default=-1)
    name = models.CharField(max_length=200, verbose_name=u"餐厅名称",default="")
    addr = models.CharField(max_length=200, verbose_name=u"地址",default="")
    price = models.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    lng = models.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    lat = models.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    cmt_num = models.IntegerField(verbose_name=u"评论数目",default=-1)
    pts = models.DecimalField(max_digits=16, verbose_name=u"评分",decimal_places=8,default=0.0)
    pts_level = models.CharField(max_length=200, verbose_name=u"评分等级",default="")
    tel = models.CharField(max_length=200, verbose_name=u"联系电话",default="", null=True)
    dishes = models.CharField(max_length=200, verbose_name=u"推荐菜",default="", null=True)
    trans = models.CharField(max_length=200, verbose_name=u"交通",default="", null=True)
    open_time = models.CharField(max_length=200, verbose_name=u"营业时间",default="", null=True)
    main_pic = models.CharField(max_length=200, verbose_name=u"餐厅主图",default="")
    url = models.TextField(verbose_name=u"url链接",default="", null=True)
    status = models.IntegerField(verbose_name=u"餐厅状态",default=-1)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name
