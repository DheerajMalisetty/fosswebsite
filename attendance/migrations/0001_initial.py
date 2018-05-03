# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-03 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('attendance', django_mysql.models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('attendance', django_mysql.models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='SSIDName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='YearlyAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('attendance', django_mysql.models.JSONField(default=dict)),
            ],
        ),
    ]
