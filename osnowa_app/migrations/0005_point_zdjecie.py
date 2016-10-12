# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osnowa_app', '0004_auto_20161009_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='zdjecie',
            field=models.ImageField(default='/static/images/znak.jpg', upload_to='static/images/'),
        ),
    ]
