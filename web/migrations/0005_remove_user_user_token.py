# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-05 21:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20180306_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_token',
        ),
    ]
