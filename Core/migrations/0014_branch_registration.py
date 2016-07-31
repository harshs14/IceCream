# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-30 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0013_auto_20160730_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.BigIntegerField()),
                ('student_number', models.IntegerField()),
                ('year', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('hosteler', models.BooleanField()),
                ('designer', models.BooleanField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Branch')),
            ],
        ),
    ]