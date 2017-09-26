# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20170926_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='place',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='place',
            name='rate',
            field=models.IntegerField(blank=True),
        ),
    ]
