# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-16 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_post_worksheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='worksheet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='collection.Worksheet'),
        ),
    ]
