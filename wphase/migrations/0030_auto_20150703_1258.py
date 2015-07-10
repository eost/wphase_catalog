# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0029_auto_20150703_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solution',
            old_name='w_az1',
            new_name='w_azm_n',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='w_az2',
            new_name='w_azm_p',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='w_az3',
            new_name='w_azm_t',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='w_eig1',
            new_name='w_eig_n',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='w_eig2',
            new_name='w_eig_p',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='w_eig3',
            new_name='w_eig_t',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='w_ia1',
            new_name='w_plg_n',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='w_ia2',
            new_name='w_plg_p',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='w_ia3',
            new_name='w_plg_t',
        ),
    ]
