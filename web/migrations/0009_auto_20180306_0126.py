# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-05 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_food_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='recipe_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='tag',
            fields=[
                ('tag_id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('tag_title', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='recipe_tag',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.tag'),
        ),
    ]
