# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default=b'draft', max_length=8, choices=[(b'draft', b'\xe8\x8d\x89\xe7\xa8\xbf'), (b'public', b'\xe5\x85\xac\xe5\xbc\x80')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(related_name='entries', to='blog.User'),
        ),
    ]
