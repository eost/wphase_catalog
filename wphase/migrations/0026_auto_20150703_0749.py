# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0025_auto_20150624_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='azp',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='cmtfile',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='solution',
            name='cth_val',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='df_val',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='dts_min',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='dts_step',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='dts_val',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='dz',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='hdsafe',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solution',
            name='ib',
            field=django.contrib.postgres.fields.ArrayField(default=[''], base_field=models.CharField(default='', max_length=7), size=None),
        ),
        migrations.AddField(
            model_name='solution',
            name='med_val_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solution',
            name='mindep',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='ntr_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solution',
            name='o_cmtf',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='solution',
            name='o_covf',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='solution',
            name='op_pa_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solution',
            name='priorsdrm0',
            field=django.contrib.postgres.fields.ArrayField(default=[0.0], base_field=models.FloatField(default=0.0), size=None),
        ),
        migrations.AddField(
            model_name='solution',
            name='ps_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solution',
            name='ref_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solution',
            name='rms_r_th',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='th_val',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='ts_nit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='solution',
            name='w_az1',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='w_az2',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='w_az3',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='w_ia1',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='w_ia2',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='w_ia3',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='xy_dx',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='solution',
            name='xy_nit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='solution',
            name='xy_nopt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='solution',
            name='xy_nx',
            field=models.IntegerField(default=0),
        ),
    ]
