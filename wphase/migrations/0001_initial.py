# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeismicEvent',
            fields=[
                ('eventid', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('EPI_agency', models.CharField(max_length=5)),
                ('EPI_year', models.IntegerField()),
                ('EPI_month', models.IntegerField()),
                ('EPI_day', models.IntegerField()),
                ('EPI_hour', models.IntegerField()),
                ('EPI_minute', models.IntegerField()),
                ('EPI_second', models.IntegerField()),
                ('EPI_latitude', models.DecimalField(max_digits=9, decimal_places=4)),
                ('EPI_longitude', models.DecimalField(max_digits=9, decimal_places=4)),
                ('EPI_depth', models.DecimalField(max_digits=6, decimal_places=1)),
                ('EPI_M1', models.DecimalField(max_digits=6, decimal_places=1)),
                ('EPI_M2', models.DecimalField(max_digits=6, decimal_places=1)),
                ('EPI_region', models.CharField(max_length=20)),
            ],
        ),
    ]
