# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-11 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cvety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metategi', models.CharField(max_length=70, verbose_name='ключевые слова')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('price', models.IntegerField()),
                ('description', models.TextField(verbose_name='описание')),
            ],
        ),
    ]