# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationadmingroup',
            name='publisher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iati_synchroniser.Publisher'),
        ),
        migrations.AlterField(
            model_name='organisationgroup',
            name='publisher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iati_synchroniser.Publisher'),
        ),
    ]