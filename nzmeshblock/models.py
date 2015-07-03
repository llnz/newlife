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
    name = models.CharField(max_length=200)
    population = models.IntegerField()
    
    area = models.PolygonField()
    
    
    objects = models.GeoManager()
    
    def __str__(self):
        return '%s (%s)' % (self.name, self.census.year)
    
    class Meta:
        unique_together = (('census', 'name'))

