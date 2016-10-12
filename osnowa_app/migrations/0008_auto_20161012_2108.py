# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osnowa_app', '0007_auto_20161012_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='zdjecie',
            field=models.ImageField(upload_to='static/images/', default='static/images/znak.jpg'),
        ),
    ]
