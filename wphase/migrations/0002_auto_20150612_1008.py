# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0004_auto_20150612_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='EPI_M1',
            new_name='epi_M1',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EPI_M2',
            new_name='epi_M2',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EPI_agency',
            new_name='epi_agency',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EPI_day',
            new_name='epi_day',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EPI_depth',
            new_name='epi_depth',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EPI_hour',
            new_name='epi_hour',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EPI_latitude',
            new_name='epi_latitude',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EPI_longitude',
            new_name='epi_longitude',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EPI_minute',
            new_name='epi_minute',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EPI_month',
            new_name='epi_month',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EPI_region',
            new_name='epi_region',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EPI_second',
            new_name='epi_second',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EPI_year',
            new_name='epi_year',
        ),
    ]
