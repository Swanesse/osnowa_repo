# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('osnowa_app', '0003_auto_20160930_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatLng',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('latit', models.FloatField()),
                ('longi', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Nazwa', max_length=256)),
                ('slug', models.SlugField()),
                ('tags', models.CharField(verbose_name='Tagi', max_length=512)),
                ('city', models.CharField(verbose_name='Miasto', max_length=32)),
                ('latlngs', models.TextField(verbose_name='Współrzędne')),
                ('distance', models.FloatField(verbose_name='Dystans')),
            ],
        ),
        migrations.RenameField(
            model_name='point',
            old_name='numer',
            new_name='numer_katalogowy',
        ),
        migrations.AddField(
            model_name='point',
            name='typ_znaku',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='point',
            name='wsp_2000',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='point',
            name='wsp_WGS84',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='point',
            name='wsp_lokalne',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='point',
            name='nazwa',
            field=models.CharField(verbose_name='Nazwa', max_length=200),
        ),
        migrations.AlterField(
            model_name='point',
            name='stabilizacja',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.CreateModel(
            name='Point2',
            fields=[
                ('latlng_ptr', models.OneToOneField(primary_key=True, to='osnowa_app.LatLng', serialize=False, parent_link=True, auto_created=True)),
                ('desc', models.CharField(max_length=120)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('osnowa_app.latlng',),
        ),
        migrations.AddField(
            model_name='map',
            name='northeast',
            field=models.ForeignKey(related_name='map_ne', to='osnowa_app.LatLng'),
        ),
        migrations.AddField(
            model_name='map',
            name='southwest',
            field=models.ForeignKey(related_name='map_sw', to='osnowa_app.LatLng'),
        ),
    ]
