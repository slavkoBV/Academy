# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-24 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0015_auto_20180806_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='order',
            field=models.PositiveSmallIntegerField(blank=True, default=1, verbose_name='Порядковий номер'),
        ),
    ]
