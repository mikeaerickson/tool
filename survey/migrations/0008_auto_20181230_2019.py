# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-30 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_tfresult_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tfresult',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]