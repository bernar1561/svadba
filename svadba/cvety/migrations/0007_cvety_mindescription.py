# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-16 05:25
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvety', '0006_auto_20170216_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvety',
            name='mindescription',
            field=ckeditor.fields.RichTextField(default=324324, verbose_name=' краткое описание'),
            preserve_default=False,
        ),
    ]