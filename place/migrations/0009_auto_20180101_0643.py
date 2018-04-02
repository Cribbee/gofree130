# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0008_eat'),
    ]

    operations = [
        migrations.AddField(
            model_name='eat',
            name='main_pic',
            field=models.CharField(default=b'', max_length=200, verbose_name='\u9910\u5385\u4e3b\u56fe'),
        ),
        migrations.AddField(
            model_name='view',
            name='main_pic',
            field=models.CharField(default=b'', max_length=200, verbose_name='\u666f\u70b9\u4e3b\u56fe'),
        ),
    ]
