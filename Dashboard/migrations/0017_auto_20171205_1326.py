# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0016_userprofile_voice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='voice',
            new_name='ai_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ai_voice',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
