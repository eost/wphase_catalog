# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0017_auto_20150615_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solution',
            old_name='m_eig1',
            new_name='w_eig1',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='m_eig2',
            new_name='w_eig2',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='m_eig3',
            new_name='w_eig3',
        ),
    ]
