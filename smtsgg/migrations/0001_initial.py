# Generated by Django 5.2.1 on 2025-07-18 02:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchCount',
            fields=[
                ('puuid', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('gamename', models.CharField(max_length=30)),
                ('tagline', models.CharField(max_length=10)),
                ('count', models.IntegerField(default=1)),
                ('latest_search', models.TimeField(default=datetime.datetime(2025, 7, 18, 2, 19, 57, 701277, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
