# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0008_auto_20150612_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='w_mpp',
            field=models.DecimalField(default=0.0, max_digits=14, decimal_places=6),
        ),
    ]
