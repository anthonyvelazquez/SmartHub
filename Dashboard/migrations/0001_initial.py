# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.TextField(default='New Profile')),
                ('first_name', models.TextField(blank=True, default=None, null=True)),
                ('last_name', models.TextField(blank=True, default=None, null=True)),
                ('age', models.TextField(blank=True, default=None, null=True)),
                ('address', models.TextField(blank=True, default=None, null=True)),
                ('loc_1', models.TextField(blank=True, default=None, null=True)),
                ('loc_2', models.TextField(blank=True, default=None, null=True)),
                ('loc_1_name', models.TextField(blank=True, default=None, null=True)),
                ('loc_2_name', models.TextField(blank=True, default=None, null=True)),
                ('current_profile', models.BooleanField(default=False)),
            ],
        ),
    ]
