# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-29 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy_news', '0003_auto_20180803_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.CharField(blank=True, max_length=200, verbose_name='Теги'),
        ),
    ]