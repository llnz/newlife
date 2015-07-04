'''
Created on 18/06/2015

@author: lee
'''
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import rest

urlpatterns = [
    #url('^$', rest.ProjectList),
    url('^census/$', rest.CensusList.as_view(), name='rest-nzmeshblock-census-list'),
    url('^census/(?P<year>[0-9]{4})/$', rest.CensusDetail.as_view(), name='rest-nzmeshblock-census-detail'),
    url('^census/(?P<year>[0-9]{4})/meshblocks', rest.MeshblockList.as_view(), name='rest-nzmeshblock-meshblock-list'),
    url('^census/(?P<year>[0-9]{4})/areas', rest.AreaList.as_view(), name='rest-nzmeshblock-area-list'),
    url('^census/(?P<year>[0-9]{4})/regions', rest.RegionList.as_view(), name='rest-nzmeshblock-region-list'),
    url('^census/(?P<year>[0-9]{4})/territory', rest.RegionList.as_view(), name='rest-nzmeshblock-territory-list'),
    
    
    url('^meshblock/(?P<pk>[0-9]+)/$', rest.MeshblockDetail.as_view(), name='rest-nzmeshblock-meshblock-detail'),
    url('^area/(?P<pk>[0-9]+)/$', rest.AreaDetail.as_view(), name='rest-nzmeshblock-area-detail'),
    url('^region/(?P<pk>[0-9]+)/$', rest.RegionDetail.as_view(), name='rest-nzmeshblock-region-detail'),
    url('^territory/(?P<pk>[0-9]+)/$', rest.TerritoryDetail.as_view(), name='rest-nzmeshblock-territory-detail'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
