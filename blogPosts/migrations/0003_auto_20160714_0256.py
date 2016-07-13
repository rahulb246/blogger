# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-13 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogPosts', '0002_auto_20160712_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='draft',
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
