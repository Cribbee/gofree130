# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_auto_20171231_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='country_id',
            field=models.IntegerField(default=-1, verbose_name='\u6240\u5c5e\u56fd\u5bb6id'),
        ),
    ]
