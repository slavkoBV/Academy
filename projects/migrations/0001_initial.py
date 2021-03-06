# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-23 10:09
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('annotation', models.TextField(help_text='Макс. 300 символів', max_length=300, verbose_name='Короткий зміст')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Зміст')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекти',
                'ordering': ('-date_created',),
            },
        ),
    ]
