# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0024_auto_20150624_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='r_np1_dip',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np1_rake',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np1_strike',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np2_dip',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np2_rake',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np2_strike',
            field=models.FloatField(),
        ),
    ]
