'''
Created on 4/07/2015

@author: lee
'''
from __future__ import unicode_literals, absolute_import, print_function

from rest_framework_gis import serializers as geo_serializers
from rest_framework import serializers

from . import models
from affordability import models as aff_models


class CensusSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rest-nzmeshblock-census-detail')
    meshblocks = serializers.HyperlinkedIdentityField(view_name='rest-nzmeshblock-meshblock-list')
    areas = serializers.HyperlinkedIdentityField(view_name='rest-nzmeshblock-area-list')
    regions = serializers.HyperlinkedIdentityField(view_name='rest-nzmeshblock-region-list')
    territories = serializers.HyperlinkedIdentityField(view_name='rest-nzmeshblock-territory-list')
    
    class Meta:
        model = models.Census
        fields = ('url', 'year', 'meshblocks', 'areas', 'regions', 'territories')

class MeshblockSerializer(geo_serializers.GeoFeatureModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rest-nzmeshblock-meshblock-detail')
    
    class Meta:
        '''Meta info the ProjectSerializer'''
        model = models.Meshblock
        geo_field = "area"
        fields = ('id', 'url', 'census', 'mb_id', 'area_unit', 'region')

class AreaSerializer(geo_serializers.GeoFeatureModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rest-nzmeshblock-area-detail')
    
    class Meta:
        '''Meta info the ProjectSerializer'''
        model = models.Area
        geo_field = "area"
        fields = ('id', 'url', 'area_name')
        
class RegionSerializer(geo_serializers.GeoFeatureModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rest-nzmeshblock-region-detail')
    
    class Meta:
        '''Meta info the ProjectSerializer'''
        model = models.Region
        geo_field = "area"
        fields = ('id', 'url', 'region_name')

class TerritorySerializer(geo_serializers.GeoFeatureModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rest-nzmeshblock-territory-detail')
    avg_rent = serializers.SerializerMethodField()
    def get_avg_rent(self, obj):
        try:
            return aff_models.Rents.objects.get(territory=obj.territory_name).avg_rent
        except aff_models.Rents.DoesNotExist:
            return 0
    
    class Meta:
        '''Meta info the ProjectSerializer'''
        model = models.Territory
        geo_field = "area"
        fields = ('id', 'url', 'territory_name', 'avg_rent')
