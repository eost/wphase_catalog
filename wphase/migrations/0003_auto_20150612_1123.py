# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0002_auto_20150612_1008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='epi_M1',
            new_name='epi_m1',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='epi_M2',
            new_name='epi_m2',
        ),
    ]
