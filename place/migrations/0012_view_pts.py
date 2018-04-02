# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0011_auto_20180101_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='view',
            name='pts',
            field=models.DecimalField(default=0.0, verbose_name='\u8bc4\u5206', max_digits=16, decimal_places=8),
        ),
    ]
