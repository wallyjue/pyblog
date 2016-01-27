# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_coverfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='coverfile',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='domain',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]