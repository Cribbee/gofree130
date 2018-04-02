# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_auto_20180101_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenic',
            name='city_id',
            field=models.IntegerField(default=3301),
            preserve_default=False,
        ),
    ]
