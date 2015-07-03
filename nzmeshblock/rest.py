'''
Created on 18/06/2015

@author: lee
'''
from __future__ import unicode_literals, absolute_import

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from . import models
from . import serialisers

class VeryLargePagePagination(PageNumberPagination):
    '''Page by 1 million items'''
    page_size = 1000000
    
class CensusList(generics.ListAPIView):
    '''REST API list view of Queries'''
    queryset = models.Census.objects.all()
    serializer_class = serialisers.CensusSerializer

class CensusDetail(generics.RetrieveAPIView):
    '''REST API detail view of a query'''
    queryset = models.Census.objects.all()
    serializer_class = serialisers.CensusSerializer

class MeshblockList(generics.ListAPIView):
    '''REST API list view of comments'''
    serializer_class = serialisers.MeshblockSerializer

    def get_queryset(self):
        census = generics.get_object_or_404(models.Census.objects.all(),
                                           year=int(self.kwargs['year']))
        return census.route_set.all()

class MeshblockDetail(generics.RetrieveAPIView):
    '''REST API detail view of comments'''
    serializer_class = serialisers.MeshblockSerializer
    queryset = models.Meshblock.objects.all()
