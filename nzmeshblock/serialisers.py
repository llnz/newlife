'''
Created on 4/07/2015

@author: lee
'''
from __future__ import unicode_literals, absolute_import, print_function

from rest_framework_gis import serializers as geo_serializers
from rest_framework import serializers

from . import models


class CensusSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rest-nzmeshblock-census-detail')
    meshblocks = serializers.HyperlinkedIdentityField(view_name='rest-nzmeshblock-meshblock-list')
    
    class Meta:
        model = models.Census
        fields = ('url', 'year', 'meshblocks')

class MeshblockSerializer(geo_serializers.GeoFeatureModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rest-nzmeshblock-meshblock-detail')
    
    class Meta:
        '''Meta info the ProjectSerializer'''
        model = models.Meshblock
        geo_field = "area"
        fields = ('id', 'url', 'census', 'name', 'population')
