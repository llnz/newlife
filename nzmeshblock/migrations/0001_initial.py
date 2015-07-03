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
                ('name', models.CharField(max_length=200)),
                ('population', models.IntegerField()),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('census', models.ForeignKey(to='nzmeshblock.Census')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='meshblock',
            unique_together=set([('census', 'name')]),
        ),
    ]
