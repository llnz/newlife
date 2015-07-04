from __future__ import absolute_import

from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Census)
admin.site.register(models.Meshblock)
admin.site.register(models.Area)
admin.site.register(models.Region)
admin.site.register(models.Territory)
