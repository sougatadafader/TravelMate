# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-17 21:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myride', '0002_auto_20180317_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='eid',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='uid',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]