# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0012_view_pts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='price',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
