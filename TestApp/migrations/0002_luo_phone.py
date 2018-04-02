# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='luo',
            name='phone',
            field=models.CharField(default=b'', max_length=30, verbose_name='\u624b\u673a'),
        ),
    ]
