# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='open_time',
            field=models.CharField(default=b'', max_length=200, null=True, verbose_name='\u5f00\u653e\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='view',
            name='tel',
            field=models.CharField(default=b'', max_length=200, null=True, verbose_name='\u8054\u7cfb\u7535\u8bdd'),
        ),
        migrations.AlterField(
            model_name='view',
            name='time_cost',
            field=models.CharField(default=b'', max_length=200, null=True, verbose_name='\u5efa\u8bae\u6e38\u89c8\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='view',
            name='way_to',
            field=models.CharField(default=b'', max_length=200, null=True, verbose_name='\u4ea4\u901a'),
        ),
    ]
