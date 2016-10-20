# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osnowa_app', '0013_point_odnaleziony'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='uszkodzony',
            field=models.IntegerField(default=0),
        ),
    ]
