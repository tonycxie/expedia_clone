# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-16 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('joiners', models.ManyToManyField(related_name='joined_trip', to='belt_app.Users')),
                ('planner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planned_trip', to='belt_app.Users')),
            ],
        ),
    ]
