# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0022_userprofile_weather_picking_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ai_gender',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
