# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_auto_20171231_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='country_id',
            field=models.IntegerField(default=-1, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x9b\xbd\xe5\xae\xb6id'),
        ),
    ]
