# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_auto_20171128_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='tank',
            name='hp_value',
            field=models.PositiveIntegerField(default=100),
        ),
    ]