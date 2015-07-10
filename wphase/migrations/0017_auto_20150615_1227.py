# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0016_auto_20150615_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='average',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='med_val',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='p2p_max',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='p2p_med',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='p2p_min',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_m0',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_m0',
            field=models.FloatField(default=0.0),
        ),
    ]
