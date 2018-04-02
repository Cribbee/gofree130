# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scenic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(unique=True, max_length=30, verbose_name='\u8d26\u53f7', db_index=True)),
                ('user_lv', models.IntegerField(null=True)),
                ('view_id', models.IntegerField()),
                ('view_name', models.CharField(max_length=30)),
                ('cmt_num', models.IntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updared', models.DateTimeField(auto_now=True)),
                ('pts', models.FloatField()),
                ('type', models.CharField(max_length=10, choices=[(b'0', b'firstTime'), (b'1', b'recommend'), (b'2', b'feedBack')])),
            ],
        ),
    ]
