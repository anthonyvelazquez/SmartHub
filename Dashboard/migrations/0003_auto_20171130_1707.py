# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_auto_20171130_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sunrise',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sunset',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
