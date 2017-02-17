# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-17 01:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_auto_20170216_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksheet',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
