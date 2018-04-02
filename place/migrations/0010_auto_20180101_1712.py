# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0009_auto_20180101_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eat',
            name='url',
            field=models.TextField(default=b'', null=True, verbose_name='url\u94fe\u63a5'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='url',
            field=models.TextField(default=b'', null=True, verbose_name='url\u94fe\u63a5'),
        ),
        migrations.AlterField(
            model_name='view',
            name='url',
            field=models.TextField(default=b'', null=True, verbose_name='url\u94fe\u63a5'),
        ),
    ]
