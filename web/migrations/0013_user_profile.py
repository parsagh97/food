# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-06 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_recipe_food_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, upload_to='recipe_images'),
        ),
    ]