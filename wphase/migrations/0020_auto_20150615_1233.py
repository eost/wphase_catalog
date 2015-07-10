# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0019_auto_20150615_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='average',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='med_val',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='p2p_max',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='p2p_med',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='p2p_min',
            field=models.FloatField(null=True),
        ),
    ]
