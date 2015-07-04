'''
Created on 4/07/2015

@author: lee
'''
from __future__ import unicode_literals, print_function, absolute_import

from django.contrib.gis.gdal import DataSource, OGRGeometry, OGRGeomType, CoordTransform
from django.db import transaction, connections, router
from django.utils import timezone


from . import models

@transaction.atomic
def meshblock_shapefile(filename, year):
    '''Import the meshblocks'''
    
    census = models.Census.objects.get_or_create(year=year)[0]
    

    ds = DataSource(filename)
    lyr = ds[0]
    
    spatial_backend = connections[router.db_for_write(models.Meshblock)].ops
    SpatialRefSys = spatial_backend.spatial_ref_sys()
    target_srs = SpatialRefSys.objects.get(srid=models.Meshblock._meta.get_field_by_name('area')[0].srid).srs
    transform = CoordTransform(lyr.srs, target_srs)
    
    for mb_item in lyr:
        with transaction.atomic():
            meshblock = models.Meshblock(census=census)
            
            g = OGRGeometry(OGRGeomType('MultiPolygon'))
            g.add(mb_item.geom)
            g.transform(transform)
            meshblock.area = g.wkt
            meshblock.mb_id = mb_item['MB2013']
            meshblock.region = mb_item['REGC2013_N']
            meshblock.territory = mb_item['TA2013_NAM']
            meshblock.area_unit = mb_item['AU2013_NAM']
            meshblock.community_board = mb_item['CB2013_NAM']
            meshblock.save()
    
@transaction.atomic
def area_shapefile(filename, year):
    '''Import the area units'''
    
    census = models.Census.objects.get_or_create(year=year)[0]
    

    ds = DataSource(filename)
    lyr = ds[0]
    
    spatial_backend = connections[router.db_for_write(models.Meshblock)].ops
    SpatialRefSys = spatial_backend.spatial_ref_sys()
    target_srs = SpatialRefSys.objects.get(srid=models.Area._meta.get_field_by_name('area')[0].srid).srs
    transform = CoordTransform(lyr.srs, target_srs)
    
    for mb_item in lyr:
        with transaction.atomic():
            area = models.Area(census=census)
            
            g = OGRGeometry(OGRGeomType('MultiPolygon'))
            g.add(mb_item.geom)
            g.transform(transform)
            area.area = g.wkt
            area.area_name = mb_item['AU2013_NAM']
            
            area.save()
    
@transaction.atomic
def region_shapefile(filename, year):
    '''Import the regions'''
    
    census = models.Census.objects.get_or_create(year=year)[0]
    

    ds = DataSource(filename)
    lyr = ds[0]
    
    spatial_backend = connections[router.db_for_write(models.Meshblock)].ops
    SpatialRefSys = spatial_backend.spatial_ref_sys()
    target_srs = SpatialRefSys.objects.get(srid=models.Region._meta.get_field_by_name('area')[0].srid).srs
    transform = CoordTransform(lyr.srs, target_srs)
    
    for mb_item in lyr:
        with transaction.atomic():
            region = models.Region(census=census)
            
            g = OGRGeometry(OGRGeomType('MultiPolygon'))
            g.add(mb_item.geom)
            g.transform(transform)
            region.area = g.wkt
            region.region_name = mb_item['REGC2013_N']
            
            region.save()
    
@transaction.atomic
def territory_shapefile(filename, year):
    '''Import the Territorial Authorities'''
    
    census = models.Census.objects.get_or_create(year=year)[0]
    

    ds = DataSource(filename)
    lyr = ds[0]
    
    spatial_backend = connections[router.db_for_write(models.Meshblock)].ops
    SpatialRefSys = spatial_backend.spatial_ref_sys()
    target_srs = SpatialRefSys.objects.get(srid=models.Territory._meta.get_field_by_name('area')[0].srid).srs
    transform = CoordTransform(lyr.srs, target_srs)
    
    for mb_item in lyr:
        with transaction.atomic():
            territory = models.Territory(census=census)
            
            g = OGRGeometry(OGRGeomType('MultiPolygon'))
            g.add(mb_item.geom)
            g.transform(transform)
            territory.area = g.wkt
            territory.territory_name = mb_item['TA2013_NAM']
            
            territory.save()
    