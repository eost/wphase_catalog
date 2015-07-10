# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0028_solution_dts_max'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='dts_max',
            field=models.FloatField(),
        ),
    ]
