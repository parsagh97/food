# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-05 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20180306_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_token',
            field=models.CharField(max_length=5),
        ),
    ]
