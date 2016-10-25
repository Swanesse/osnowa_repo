# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osnowa_app', '0014_point_uszkodzony'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='h_amsterdam',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='point',
            name='h_kronsztadt_86',
            field=models.CharField(default='', max_length=200),
        ),
    ]
