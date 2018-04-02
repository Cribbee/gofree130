# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0006_auto_20171231_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_id', models.IntegerField(default=-1, verbose_name='\u6240\u5c5e\u56fd\u5bb6id')),
                ('province_id', models.IntegerField(default=-1, verbose_name='\u6240\u5c5e\u7701\u4efdid')),
                ('city_id', models.IntegerField(default=-1, verbose_name='\u6240\u5c5e\u57ce\u5e02id')),
                ('district_id', models.IntegerField(default=-1, verbose_name='\u6240\u5c5e\u884c\u653f\u533aid')),
                ('name', models.CharField(default=b'', max_length=200, verbose_name='\u9152\u5e97\u540d\u79f0')),
                ('en_name', models.CharField(default=b'', max_length=200, verbose_name='\u9152\u5e97\u82f1\u6587\u540d\u79f0')),
                ('addr', models.CharField(default=b'', max_length=200, verbose_name='\u9152\u5e97\u5730\u5740')),
                ('price', models.DecimalField(default=0.0, max_digits=16, decimal_places=8)),
                ('lng', models.DecimalField(default=0.0, max_digits=16, decimal_places=8)),
                ('lat', models.DecimalField(default=0.0, max_digits=16, decimal_places=8)),
                ('cmt_num', models.IntegerField(default=-1, verbose_name='\u8bc4\u8bba\u6570\u76ee')),
                ('pts', models.DecimalField(default=0.0, verbose_name='\u8bc4\u5206', max_digits=16, decimal_places=8)),
                ('pts_level', models.CharField(default=b'', max_length=200, verbose_name='\u8bc4\u5206\u7b49\u7ea7')),
                ('note_num', models.IntegerField(default=-1, verbose_name='\u6e38\u8bb0\u6570\u76ee')),
                ('desc', models.CharField(default=b'', max_length=200, verbose_name='\u63cf\u8ff0')),
                ('main_pic', models.CharField(default=b'', max_length=200, verbose_name='\u9152\u5e97\u4e3b\u56fe')),
                ('url', models.CharField(default=b'', max_length=200, null=True, verbose_name='url\u94fe\u63a5')),
                ('status', models.IntegerField(default=-1, verbose_name='\u9152\u5e97\u72b6\u6001')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
