# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-17 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('rating', models.FloatField(default=5.0)),
            ],
        ),
    ]
