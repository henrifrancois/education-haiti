# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-19 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160613_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='article_picture',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='img'),
        ),
    ]
