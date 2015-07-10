# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0023_auto_20150617_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='r_np1_dip',
            field=models.DecimalField(max_digits=3, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np1_rake',
            field=models.DecimalField(max_digits=5, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np1_strike',
            field=models.DecimalField(max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np2_dip',
            field=models.DecimalField(max_digits=3, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np2_rake',
            field=models.DecimalField(max_digits=5, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np2_strike',
            field=models.DecimalField(max_digits=4, decimal_places=1),
        ),
    ]
