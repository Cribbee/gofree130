# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0004_auto_20171231_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='view',
            name='url',
            field=models.CharField(default=b'', max_length=200, null=True, verbose_name='url\u94fe\u63a5'),
        ),
    ]
