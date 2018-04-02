# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_view_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='view',
            old_name='way_to',
            new_name='trans',
        ),
        migrations.AddField(
            model_name='view',
            name='addr',
            field=models.CharField(default=b'', max_length=200, verbose_name='\u5730\u5740'),
        ),
    ]
