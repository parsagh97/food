# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-05 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180306_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.CharField(max_length=5)),
                ('food_title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=5),
        ),
    ]
