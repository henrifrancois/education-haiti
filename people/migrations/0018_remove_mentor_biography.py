# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-17 22:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0017_mentor_biography'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='biography',
        ),
    ]
