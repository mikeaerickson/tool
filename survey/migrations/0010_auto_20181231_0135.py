# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-31 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_design_none_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='att10_name',
            field=models.CharField(blank=True, default=b'', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='att10_type',
            field=models.IntegerField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='design',
            name='att1_name',
            field=models.CharField(blank=True, default=b'', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='att1_type',
            field=models.IntegerField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='design',
            name='att2_name',
            field=models.CharField(blank=True, default=b'', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='att2_type',
            field=models.IntegerField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='design',
            name='att3_name',
            field=models.CharField(blank=True, default=b'', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='att3_type',
            field=models.IntegerField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='design',
            name='att4_name',
            field=models.CharField(blank=True, default=b'', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='att4_type',
            field=models.IntegerField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='design',
            name='att5_name',
            field=models.CharField(blank=True, default=b'', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='att5_type',
            field=models.IntegerField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='design',
            name='att6_name',
            field=models.CharField(blank=True, default=b'', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='att6_type',
            field=models.IntegerField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='design',
            name='att7_name',
            field=models.CharField(blank=True, default=b'', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='att7_type',
            field=models.IntegerField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='design',
            name='att8_name',
            field=models.CharField(blank=True, default=b'', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='att8_type',
            field=models.IntegerField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='design',
            name='att9_name',
            field=models.CharField(blank=True, default=b'', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='att9_type',
            field=models.IntegerField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='design',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
