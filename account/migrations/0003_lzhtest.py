# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20171224_0548'),
    ]

    operations = [
        migrations.CreateModel(
            name='lzhTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=30, verbose_name='this is \u8d26\u53f7', db_index=True)),
                ('password', models.CharField(max_length=200, verbose_name='this is\u5bc6\u7801')),
                ('phone', models.CharField(default=b'', max_length=30, verbose_name='this is\u624b\u673a')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('sex', models.CharField(max_length=10, null=True, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('age', models.SmallIntegerField(default=-1, blank=True)),
            ],
        ),
    ]
