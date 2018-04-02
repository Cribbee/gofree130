# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0013_auto_20180102_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='trans',
            field=models.TextField(default=b'', null=True, verbose_name='\u4ea4\u901a\u8def\u7ebf'),
        ),
    ]
