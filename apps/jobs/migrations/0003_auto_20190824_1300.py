# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-08-24 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190824_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_address', to='jobs.Location'),
        ),
    ]
