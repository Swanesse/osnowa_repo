# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('osnowa_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('arkusz_mapy', models.TextField()),
                ('nazwa', models.TextField()),
                ('klasa', models.TextField()),
                ('numer', models.CharField(max_length=200)),
                ('wojewodztwo', models.TextField()),
                ('powiat', models.TextField()),
                ('gmina', models.TextField()),
                ('miejscowosc', models.TextField()),
                ('stabilizacja', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('find_date', models.DateTimeField(blank=True, null=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='punkt',
            name='autor',
        ),
        migrations.DeleteModel(
            name='Punkt',
        ),
    ]
