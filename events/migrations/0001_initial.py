# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-02 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('date', models.DateField()),
                ('slug', models.SlugField(max_length=140)),
                ('number_of_participants', models.IntegerField()),
                ('number_of_attendees', models.IntegerField(default=0)),
                ('created_on', models.DateField(auto_now=True)),
                ('language', models.CharField(choices=[('EN', 'ENGLISH'), ('FR', 'FRENCH')], default='EN', max_length=2)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='attendee',
            name='events',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
    ]
