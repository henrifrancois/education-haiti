# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-12 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20160612_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='mentees',
            field=models.ManyToManyField(to='people.Mentee'),
        ),
    ]
