# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osnowa_app', '0005_point_zdjecie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='zdjecie',
            field=models.ImageField(upload_to=''),
        ),
    ]
