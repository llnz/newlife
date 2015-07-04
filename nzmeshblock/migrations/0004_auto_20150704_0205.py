# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nzmeshblock', '0003_auto_20150704_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('territory_name', models.CharField(max_length=200)),
                ('area', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('census', models.ForeignKey(to='nzmeshblock.Census')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='territory',
            unique_together=set([('census', 'territory_name')]),
        ),
    ]
