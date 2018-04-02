# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20180101_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scenic',
            old_name='updared',
            new_name='updated',
        ),
    ]
