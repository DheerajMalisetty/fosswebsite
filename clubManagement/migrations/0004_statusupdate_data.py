# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubManagement', '0003_statusupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusupdate',
            name='data',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
