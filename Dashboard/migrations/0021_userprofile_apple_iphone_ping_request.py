# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0020_userprofile_apple_iphone_dev_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='apple_iphone_ping_request',
            field=models.BooleanField(default=False),
        ),
    ]
