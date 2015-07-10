# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0009_solution_w_mpp'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='r_mpp',
            field=models.DecimalField(default=0.0, max_digits=14, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_mpp',
            field=models.DecimalField(max_digits=14, decimal_places=6),
        ),
    ]
