# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wphase', '0006_remove_event_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='comments',
            field=django.contrib.postgres.fields.ArrayField(default=[''], base_field=models.CharField(default='', max_length=50), size=None),
        ),
    ]
