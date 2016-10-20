# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osnowa_app', '0012_auto_20161013_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='odnaleziony',
            field=models.IntegerField(default=0),
        ),
    ]
