# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0021_solution_gf_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='cond_thre',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='solution',
            name='damp_fac',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='solution',
            name='dmax',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='dmin',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='filt_cf1',
            field=models.DecimalField(max_digits=7, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='solution',
            name='filt_cf2',
            field=models.DecimalField(max_digits=7, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='solution',
            name='filt_order',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='filt_pass',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='gap',
            field=models.DecimalField(max_digits=5, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='nb_channels',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='nb_rejected_channels',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='nb_stations',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_depth',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_eig1',
            field=models.DecimalField(max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_eig2',
            field=models.DecimalField(max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_eig3',
            field=models.DecimalField(max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_half_duration',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_latitude',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_longitude',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_m0',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_mpp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_mrp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_mrr',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_mrt',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_mtp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_mtt',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_mw',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np1_dip',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np1_rake',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np1_strike',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np2_dip',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np2_rake',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_np2_strike',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='r_time_shift',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='rrms',
            field=models.DecimalField(max_digits=9, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='solution',
            name='rrms_r',
            field=models.DecimalField(max_digits=9, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_depth',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_eig1',
            field=models.DecimalField(max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_eig2',
            field=models.DecimalField(max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_eig3',
            field=models.DecimalField(max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_half_duration',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_latitude',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_longitude',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_m0',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_mpp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_mrp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_mrr',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_mrt',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_mtp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_mtt',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_mw',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_np1_dip',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_np1_rake',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_np1_strike',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_np2_dip',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_np2_rake',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_np2_strike',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='solution',
            name='w_time_shift',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='we',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='wn',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='solution',
            name='wrms',
            field=models.DecimalField(max_digits=9, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='solution',
            name='wrms_r',
            field=models.DecimalField(max_digits=9, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='solution',
            name='wz',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
    ]
