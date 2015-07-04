from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Rents(models.Model):
    date = models.DateField()
    territory = models.CharField(max_length=100)
    avg_rent = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return '%s (%s)' % (self.territory, self.date)

