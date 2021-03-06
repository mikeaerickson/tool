# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-27 21:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datefilled', models.DateTimeField(auto_now_add=True)),
                ('responses', models.CharField(max_length=250)),
                ('metaData1', models.CharField(max_length=100)),
                ('metaData2', models.CharField(max_length=100)),
                ('metaData3', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parthworths', models.CharField(max_length=250)),
                ('tfmodel', models.CharField(max_length=250)),
                ('dategenerated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=250)),
                ('questions', models.CharField(max_length=250)),
                ('profiles', models.CharField(max_length=250)),
                ('in_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='survey.Study')),
            ],
        ),
        migrations.AddField(
            model_name='results',
            name='for_survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='survey.Survey'),
        ),
        migrations.AddField(
            model_name='response',
            name='for_survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='survey.Survey'),
        ),
    ]
