# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-12 04:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20200312_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='published_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
