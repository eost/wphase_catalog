# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0018_auto_20150615_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='cond_number',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=1),
        ),
    ]
