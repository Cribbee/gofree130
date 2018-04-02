# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_id', models.IntegerField(default=-1, verbose_name='\u6240\u5c5e\u56fd\u5bb6id')),
                ('province_id', models.IntegerField(default=-1, verbose_name='\u6240\u5c5e\u7701\u4efdid')),
                ('city_id', models.IntegerField(default=-1, verbose_name='\u6240\u5c5e\u57ce\u5e02id')),
                ('district_id', models.IntegerField(default=-1, verbose_name='\u6240\u5c5e\u884c\u653f\u533aid')),
                ('name', models.CharField(default=b'', max_length=200, verbose_name='\u666f\u70b9\u540d\u79f0')),
                ('price', models.DecimalField(default=0.0, max_digits=16, decimal_places=8)),
                ('lng', models.DecimalField(default=0.0, max_digits=16, decimal_places=8)),
                ('lat', models.DecimalField(default=0.0, max_digits=16, decimal_places=8)),
                ('cmt_num', models.IntegerField(default=-1, verbose_name='\u8bc4\u8bba\u6570\u76ee')),
                ('tel', models.CharField(default=b'', max_length=200, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('time_cost', models.CharField(default=b'', max_length=200, verbose_name='\u5efa\u8bae\u6e38\u89c8\u65f6\u95f4')),
                ('way_to', models.CharField(default=b'', max_length=200, verbose_name='\u4ea4\u901a')),
                ('open_time', models.CharField(default=b'', max_length=200, verbose_name='\u5f00\u653e\u65f6\u95f4')),
                ('status', models.IntegerField(default=-1, verbose_name='\u666f\u70b9\u72b6\u6001')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
