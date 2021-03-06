# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField()),
                ('start_date', models.CharField(max_length=20)),
                ('end_date', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
