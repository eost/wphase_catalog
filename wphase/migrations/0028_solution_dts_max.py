# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0027_auto_20150703_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='dts_max',
            field=models.FloatField(default=0.0),
        ),
    ]
