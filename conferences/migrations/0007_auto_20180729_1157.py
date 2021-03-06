# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0006_auto_20180724_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='thesis_file',
            field=models.FileField(blank=True, null=True, upload_to='thesises/%Y-%m-%d', verbose_name='Збірка доповідей'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='information_message',
            field=models.FileField(blank=True, null=True, upload_to='inform_messages/%Y/%m/%d', verbose_name='Інформаційне повідомлення'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(choices=[('Природничі науки', 'Природничі науки'), ('Інформаційні технології', 'Інформаційні технології'), ('Механічна інженерія', 'Механічна інженерія'), ('Електрична інженерія', 'Електрична інженерія'), ('Автоматизація та приладобудування', 'Автоматизація та приладобудування'), ('Хімічна та біоінженерія', 'Хімічна та біоінженерія'), ('Електроніка та телекомунікації', 'Електроніка та телекомунікації'), ('Виробництво та технології', 'Виробництво та технології'), ('Архітектура та будівництв о', 'Архітектура та будівництво'), ('Цивільна безпека', 'Цивільна безпека'), ('Транспорт', 'Транспорт')], max_length=100, verbose_name='Назва секції'),
        ),
        migrations.AlterField(
            model_name='thesis',
            name='section',
            field=models.CharField(choices=[('Природничі науки', 'Природничі науки'), ('Інформаційні технології', 'Інформаційні технології'), ('Механічна інженерія', 'Механічна інженерія'), ('Електрична інженерія', 'Електрична інженерія'), ('Автоматизація та приладобудування', 'Автоматизація та приладобудування'), ('Хімічна та біоінженерія', 'Хімічна та біоінженерія'), ('Електроніка та телекомунікації', 'Електроніка та телекомунікації'), ('Виробництво та технології', 'Виробництво та технології'), ('Архітектура та будівництв о', 'Архітектура та будівництво'), ('Цивільна безпека', 'Цивільна безпека'), ('Транспорт', 'Транспорт')], default=('Природничі науки', 'Природничі науки'), max_length=100, verbose_name='Назва секції'),
        ),
    ]
