# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2020-04-16 07:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0048_auto_20190927_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='github_username',
            field=models.CharField(default='', max_length=39, validators=[django.core.validators.RegexValidator(regex='^[a-z\\d](?:[a-z\\d]|-(?=[a-z\\d])){0,38}$')]),
        ),
    ]
