# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0012_auto_20150615_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='stations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=20), size=None),
        ),
    ]
