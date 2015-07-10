# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0015_auto_20150615_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='r_mpp',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_mrp',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_mrr',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_mrt',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_mtp',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_mtt',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_mpp',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_mrp',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_mrt',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_mtp',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_mtt',
            field=models.FloatField(default=0.0),
        ),
    ]
