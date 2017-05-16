# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-16 22:28
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20170515_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, null=True, upload_to='media', verbose_name='Image'),
        ),
    ]