# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0014_auto_20150615_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='w_mrr',
            field=models.FloatField(default=0.0),
        ),
    ]
