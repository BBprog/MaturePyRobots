# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_auto_20171128_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='next_level_exp',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
