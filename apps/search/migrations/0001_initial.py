# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-22 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_number', models.IntegerField()),
                ('account_suffix', models.CharField(default='z', max_length=5)),
                ('cust_name', models.CharField(max_length=255)),
                ('url_begin', models.TextField()),
                ('url_end', models.TextField()),
                ('catalog_type', models.CharField(default='B', max_length=25)),
                ('element', models.CharField(max_length=255)),
            ],
        ),
    ]
