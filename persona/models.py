#coding:utf-8
from django.db import models

"""
        Summary of class here.

        Longer class information....
        Longer class information....

        Attributes:
            likes_spam: A boolean indicating if we like SPAM or not.
            eggs: An integer count of the eggs we have laid.
        Author: lxy
        BuildDate:00:35:16
        Version:0.1
        Date:2017-12-28
        History:
"""

class Scenic(models.Model):
    
    user_id = models.IntegerField(null=False)
    user_name = models.CharField(max_length=30, verbose_name=u"账号")
    # 用户等级
    user_lv = models.IntegerField(null=True)
    # 景点id
    view_id = models.IntegerField(null=False)
    # 景点名
    view_name = models.CharField(max_length=30)
    # 景点所属城市id
    city_id = models.IntegerField(null=False)
    # 该景点评论数
    cmt_num = models.IntegerField(null=True)
    # 偏好记录建立时间
    created = models.DateTimeField(auto_now_add=True)
    # 更新建立时间
    updated = models.DateTimeField(auto_now=True)
    # 评分
    pts = models.FloatField()
    # 评价类型 0-初始选择 1-系统推荐 2-用户反馈评价
    TYPE_CHOICES = (('0','firstTime'),('1','recommend'),('2','feedBack'))
    type = models.CharField(max_length=10,choices=TYPE_CHOICES)
   
    def __str__(self):
        return self.view_name

