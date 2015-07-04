from __future__ import unicode_literals, absolute_import

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Census(models.Model):
    year = models.IntegerField()
    
    def __str__(self):
        return '%s' % self.year
    

@python_2_unicode_compatible
class Meshblock(models.Model):
    census = models.ForeignKey(Census)
    mb_id = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    territory = models.CharField(max_length=100)
    community_board = models.CharField(max_length=100)
    area_unit = models.CharField(max_length=200)
    
    
    
    area = models.MultiPolygonField(srid=4326)
    
    
    objects = models.GeoManager()
    
    def __str__(self):
        return '%s (%s)' % (self.mb_id, self.census.year)
    
    class Meta:
        unique_together = (('census', 'mb_id'))

@python_2_unicode_compatible
class Area(models.Model):
    census = models.ForeignKey(Census)
    area_name = models.CharField(max_length=200)
    
    area = models.MultiPolygonField(srid=4326)
    
    
    objects = models.GeoManager()
    
    def __str__(self):
        return '%s (%s)' % (self.area_name, self.census.year)
    
    class Meta:
        unique_together = (('census', 'area_name'))

@python_2_unicode_compatible
class Region(models.Model):
    census = models.ForeignKey(Census)
    region_name = models.CharField(max_length=200)
    
    area = models.MultiPolygonField(srid=4326)
    
    
    objects = models.GeoManager()
    
    def __str__(self):
        return '%s (%s)' % (self.region_name, self.census.year)
    
    class Meta:
        unique_together = (('census', 'region_name'))

@python_2_unicode_compatible
class Territory(models.Model):
    census = models.ForeignKey(Census)
    territory_name = models.CharField(max_length=200)
    
    area = models.MultiPolygonField(srid=4326)
    
    
    objects = models.GeoManager()
    
    def __str__(self):
        return '%s (%s)' % (self.territory_name, self.census.year)
    
    class Meta:
        unique_together = (('census', 'territory_name'))
