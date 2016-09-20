# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Punkt',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('find_date', models.DateTimeField(null=True, blank=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
