# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-03 21:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20160803_2055'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendee',
        ),
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='attendees', to=settings.AUTH_USER_MODEL),
        ),
    ]
