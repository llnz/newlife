# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Census',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meshblock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mb_id', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=100)),
                ('territory', models.CharField(max_length=100)),
                ('community_board', models.CharField(max_length=100)),
                ('area_unit', models.CharField(max_length=200)),
                ('area', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('census', models.ForeignKey(to='nzmeshblock.Census')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='meshblock',
            unique_together=set([('census', 'mb_id')]),
        ),
    ]
