# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-30 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20181230_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('num_alts', models.IntegerField()),
                ('num_qs', models.IntegerField()),
                ('att1_name', models.CharField(max_length=30, unique=True)),
                ('att1_type', models.IntegerField()),
                ('att2_name', models.CharField(max_length=30, unique=True)),
                ('att2_type', models.IntegerField()),
                ('att3_name', models.CharField(max_length=30, unique=True)),
                ('att3_type', models.IntegerField()),
                ('att4_name', models.CharField(max_length=30, unique=True)),
                ('att4_type', models.IntegerField()),
                ('att5_name', models.CharField(max_length=30, unique=True)),
                ('att5_type', models.IntegerField()),
                ('att6_name', models.CharField(max_length=30, unique=True)),
                ('att6_type', models.IntegerField()),
                ('att7_name', models.CharField(max_length=30, unique=True)),
                ('att7_type', models.IntegerField()),
                ('att8_name', models.CharField(max_length=30, unique=True)),
                ('att8_type', models.IntegerField()),
                ('att9_name', models.CharField(max_length=30, unique=True)),
                ('att9_type', models.IntegerField()),
                ('att10_name', models.CharField(max_length=30, unique=True)),
                ('att10_type', models.IntegerField()),
                ('in_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='design', to='survey.Survey')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('Q1A1', models.IntegerField()),
                ('Q1A2', models.IntegerField()),
                ('Q1A3', models.IntegerField()),
                ('Q1A4', models.IntegerField()),
                ('Q2A1', models.IntegerField()),
                ('Q2A2', models.IntegerField()),
                ('Q2A3', models.IntegerField()),
                ('Q2A4', models.IntegerField()),
                ('Q3A1', models.IntegerField()),
                ('Q3A2', models.IntegerField()),
                ('Q3A3', models.IntegerField()),
                ('Q3A4', models.IntegerField()),
                ('Q4A1', models.IntegerField()),
                ('Q4A2', models.IntegerField()),
                ('Q4A3', models.IntegerField()),
                ('Q4A4', models.IntegerField()),
                ('Q5A1', models.IntegerField()),
                ('Q5A2', models.IntegerField()),
                ('Q5A3', models.IntegerField()),
                ('Q5A4', models.IntegerField()),
                ('Q6A1', models.IntegerField()),
                ('Q6A2', models.IntegerField()),
                ('Q6A3', models.IntegerField()),
                ('Q6A4', models.IntegerField()),
                ('Q7A1', models.IntegerField()),
                ('Q7A2', models.IntegerField()),
                ('Q7A3', models.IntegerField()),
                ('Q7A4', models.IntegerField()),
                ('Q8A1', models.IntegerField()),
                ('Q8A2', models.IntegerField()),
                ('Q8A3', models.IntegerField()),
                ('Q8A4', models.IntegerField()),
                ('Q9A1', models.IntegerField()),
                ('Q9A2', models.IntegerField()),
                ('Q9A3', models.IntegerField()),
                ('Q9A4', models.IntegerField()),
                ('Q10A1', models.IntegerField()),
                ('Q10A2', models.IntegerField()),
                ('Q10A3', models.IntegerField()),
                ('Q10A4', models.IntegerField()),
                ('Q11A1', models.IntegerField()),
                ('Q11A2', models.IntegerField()),
                ('Q11A3', models.IntegerField()),
                ('Q11A4', models.IntegerField()),
                ('Q12A1', models.IntegerField()),
                ('Q12A2', models.IntegerField()),
                ('Q12A3', models.IntegerField()),
                ('Q12A4', models.IntegerField()),
                ('Q13A1', models.IntegerField()),
                ('Q13A2', models.IntegerField()),
                ('Q13A3', models.IntegerField()),
                ('Q13A4', models.IntegerField()),
                ('Q14A1', models.IntegerField()),
                ('Q14A2', models.IntegerField()),
                ('Q14A3', models.IntegerField()),
                ('Q14A4', models.IntegerField()),
                ('Q15A1', models.IntegerField()),
                ('Q15A2', models.IntegerField()),
                ('Q15A3', models.IntegerField()),
                ('Q15A4', models.IntegerField()),
                ('Q16A1', models.IntegerField()),
                ('Q16A2', models.IntegerField()),
                ('Q16A3', models.IntegerField()),
                ('Q16A4', models.IntegerField()),
                ('Q17A1', models.IntegerField()),
                ('Q17A2', models.IntegerField()),
                ('Q17A3', models.IntegerField()),
                ('Q17A4', models.IntegerField()),
                ('Q18A1', models.IntegerField()),
                ('Q18A2', models.IntegerField()),
                ('Q18A3', models.IntegerField()),
                ('Q18A4', models.IntegerField()),
                ('Q19A1', models.IntegerField()),
                ('Q19A2', models.IntegerField()),
                ('Q19A3', models.IntegerField()),
                ('Q19A4', models.IntegerField()),
                ('Q20A1', models.IntegerField()),
                ('Q20A2', models.IntegerField()),
                ('Q20A3', models.IntegerField()),
                ('Q20A4', models.IntegerField()),
                ('in_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='survey.Survey')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q1', models.IntegerField()),
                ('Q2', models.IntegerField()),
                ('Q3', models.IntegerField()),
                ('Q4', models.IntegerField()),
                ('Q5', models.IntegerField()),
                ('Q6', models.IntegerField()),
                ('Q7', models.IntegerField()),
                ('Q8', models.IntegerField()),
                ('Q9', models.IntegerField()),
                ('Q10', models.IntegerField()),
                ('Q11', models.IntegerField()),
                ('Q12', models.IntegerField()),
                ('Q13', models.IntegerField()),
                ('Q14', models.IntegerField()),
                ('Q15', models.IntegerField()),
                ('Q16', models.IntegerField()),
                ('Q17', models.IntegerField()),
                ('Q18', models.IntegerField()),
                ('Q19', models.IntegerField()),
                ('Q20', models.IntegerField()),
            ],
        ),
    ]