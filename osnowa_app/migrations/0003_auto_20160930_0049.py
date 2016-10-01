# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osnowa_app', '0002_auto_20160920_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='arkusz_mapy',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='point',
            name='gmina',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='point',
            name='klasa',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='point',
            name='miejscowosc',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='point',
            name='nazwa',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='point',
            name='powiat',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='point',
            name='stabilizacja',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='point',
            name='wojewodztwo',
            field=models.CharField(max_length=200),
        ),
    ]
