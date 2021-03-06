# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 17:04
from __future__ import unicode_literals

import conferences.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0012_auto_20180729_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='information_message',
            field=models.FileField(blank=True, null=True, upload_to=conferences.models.get_upload_path, verbose_name='Інформаційне повідомлення'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='thesis_file',
            field=models.FileField(blank=True, null=True, upload_to=conferences.models.get_upload_path, verbose_name='Збірка доповідей'),
        ),
    ]
