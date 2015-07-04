# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nzmeshblock', '0002_auto_20150704_0135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region_name', models.CharField(max_length=200)),
                ('area', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('census', models.ForeignKey(to='nzmeshblock.Census')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='region',
            unique_together=set([('census', 'region_name')]),
        ),
    ]
