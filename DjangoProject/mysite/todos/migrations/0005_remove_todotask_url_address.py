# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 13:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_todotask_url_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todotask',
            name='url_address',
        ),
    ]
