# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-14 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Ordered', 'Ordered'), ('Processed', 'Processed')], default='Ordered', max_length=1),
        ),
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]