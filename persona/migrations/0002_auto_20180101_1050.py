# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenic',
            name='user_name',
            field=models.CharField(max_length=30, verbose_name='\u8d26\u53f7'),
        ),
    ]
