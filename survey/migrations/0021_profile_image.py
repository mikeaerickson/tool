# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-06 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0020_auto_20190105_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
