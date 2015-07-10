# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0011_auto_20150615_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='dc_flag',
            field=models.NullBooleanField(),
        ),
    ]
