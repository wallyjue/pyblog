# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160124_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='mediafile',
        ),
        migrations.AddField(
            model_name='media',
            name='file',
            field=models.FileField(null=True, upload_to='%Y/%m/%d'),
        ),
    ]
