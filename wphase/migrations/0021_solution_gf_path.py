# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0020_auto_20150615_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='gf_path',
            field=models.CharField(default='', max_length=50),
        ),
    ]
