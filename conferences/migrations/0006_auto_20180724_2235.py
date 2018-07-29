# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-24 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0005_auto_20180724_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(choices=[('Природничі науки', 'Природничі науки'), ('Інформаційні технології', 'Інформаційні технології'), ('Механічна інженерія', 'Механічна інженерія'), ('Електрична інженерія', 'Електрична інженерія'), ('Автоматизація та приладобудування', 'Автоматизація та приладобудування'), ('Хімічна та біоінженерія', 'Хімічна та біоінженерія'), ('Електроніка та телекомунікації', 'Електроніка та телекомунікації'), ('Виробництво та технології', 'Виробництво та технології'), ('Архітектура та будівництво', 'Архітектура та будівництво'), ('Цивільна безпека', 'Цивільна безпека'), ('Транспорт', 'Транспорт')], max_length=100, verbose_name='Назва секції'),
        ),
        migrations.AlterField(
            model_name='thesis',
            name='section',
            field=models.CharField(choices=[('Природничі науки', 'Природничі науки'), ('Інформаційні технології', 'Інформаційні технології'), ('Механічна інженерія', 'Механічна інженерія'), ('Електрична інженерія', 'Електрична інженерія'), ('Автоматизація та приладобудування', 'Автоматизація та приладобудування'), ('Хімічна та біоінженерія', 'Хімічна та біоінженерія'), ('Електроніка та телекомунікації', 'Електроніка та телекомунікації'), ('Виробництво та технології', 'Виробництво та технології'), ('Архітектура та будівництво', 'Архітектура та будівництво'), ('Цивільна безпека', 'Цивільна безпека'), ('Транспорт', 'Транспорт')], default=('Природничі науки', 'Природничі науки'), max_length=100, verbose_name='Назва секції'),
        ),
    ]