# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-28 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0012_auto_20160726_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='expires',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='subject',
            field=models.CharField(max_length=200),
        ),
    ]
