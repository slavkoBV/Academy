# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 16:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_auto_20180712_1810'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='thesis',
            unique_together=set([('title', 'conference')]),
        ),
    ]
