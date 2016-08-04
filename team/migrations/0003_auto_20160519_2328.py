# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 23:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20160519_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='member',
            field=models.ManyToManyField(blank=True, null=True, related_name='team_member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='service',
            field=models.ManyToManyField(blank=True, null=True, related_name='team_service', to='team.Service'),
        ),
    ]
