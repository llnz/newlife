# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nzmeshblock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_name', models.CharField(max_length=200)),
                ('area', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('census', models.ForeignKey(to='nzmeshblock.Census')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='area',
            unique_together=set([('census', 'area_name')]),
        ),
    ]
