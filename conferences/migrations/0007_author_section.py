# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0006_auto_20180722_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='section',
            field=models.CharField(choices=[('Природничі науки', 'Природничі науки'), ('Інформаційні технології', 'Інформаційні технології'), ('Механічна інженерія', 'Механічна інженерія'), ('Електрична інженерія', 'Електрична інженерія'), ('Автоматизація та приладобудування', 'Автоматизація та приладобудування'), ('Хімічна та біоінженерія', 'Хімічна та біоінженерія'), ('Електроніка та телекомунікації', 'Електроніка та телекомунікації'), ('Виробництво та технології', 'Виробництво та технології'), ('Архітектура та будівництво', 'Архітектура та будівництво'), ('Цивільна безпека', 'Цивільна безпека'), ('Транспорт', 'Транспорт')], default='None', max_length=35, verbose_name='Назва секції'),
        ),
    ]
