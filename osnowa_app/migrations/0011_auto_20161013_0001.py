# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osnowa_app', '0010_auto_20161012_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='zdjecie',
            field=models.ImageField(default='static/images/znak.jpg', upload_to='public/static/images/'),
        ),
    ]
