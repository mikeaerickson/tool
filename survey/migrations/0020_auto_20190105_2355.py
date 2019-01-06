# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-05 23:55
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0019_design_att1_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='att10_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=4, max_digits=5), null=True, size=10),
        ),
        migrations.AddField(
            model_name='design',
            name='att2_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=4, max_digits=5), null=True, size=10),
        ),
        migrations.AddField(
            model_name='design',
            name='att3_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=4, max_digits=5), null=True, size=10),
        ),
        migrations.AddField(
            model_name='design',
            name='att4_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=4, max_digits=5), null=True, size=10),
        ),
        migrations.AddField(
            model_name='design',
            name='att5_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=4, max_digits=5), null=True, size=10),
        ),
        migrations.AddField(
            model_name='design',
            name='att6_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=4, max_digits=5), null=True, size=10),
        ),
        migrations.AddField(
            model_name='design',
            name='att7_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=4, max_digits=5), null=True, size=10),
        ),
        migrations.AddField(
            model_name='design',
            name='att8_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=4, max_digits=5), null=True, size=10),
        ),
        migrations.AddField(
            model_name='design',
            name='att9_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=4, max_digits=5), null=True, size=10),
        ),
    ]
