# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='publish_date',
            field=models.DateTimeField(editable=False, verbose_name='date published'),
        ),
    ]