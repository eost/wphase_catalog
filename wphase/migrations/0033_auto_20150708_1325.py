# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0032_auto_20150708_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='epi_region',
            field=models.CharField(max_length=32),
        ),
    ]
