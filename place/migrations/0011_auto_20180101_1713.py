# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0010_auto_20180101_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eat',
            name='district_id',
        ),
        migrations.RemoveField(
            model_name='eat',
            name='province_id',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='district_id',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='province_id',
        ),
        migrations.RemoveField(
            model_name='view',
            name='district_id',
        ),
        migrations.RemoveField(
            model_name='view',
            name='province_id',
        ),
    ]
