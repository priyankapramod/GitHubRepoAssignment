# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='review',
            field=models.CharField(max_length=500),
        ),
    ]
