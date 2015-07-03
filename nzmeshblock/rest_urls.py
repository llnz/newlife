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
    
    url('^meshblock/(?P<pk>[0-9]+)/$', rest.MeshblockDetail.as_view(), name='rest-nzmeshblock-meshblock-detail'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
