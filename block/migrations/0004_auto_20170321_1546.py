# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0003_auto_20170321_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='block',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
