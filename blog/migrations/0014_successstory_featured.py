# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-26 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160718_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='successstory',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]