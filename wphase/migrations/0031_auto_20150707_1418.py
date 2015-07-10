# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0030_auto_20150703_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solution',
            old_name='r_eig1',
            new_name='r_eig_n',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='r_eig2',
            new_name='r_eig_p',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='r_eig3',
            new_name='r_eig_t',
        ),
    ]
