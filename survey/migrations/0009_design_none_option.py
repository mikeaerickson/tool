# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-31 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_remove_survey_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='none_option',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
