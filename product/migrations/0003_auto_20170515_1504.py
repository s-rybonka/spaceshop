# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-15 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20170515_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Image'),
        ),
    ]
