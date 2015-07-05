'''
Created on 4/07/2015

@author: lee
'''
from __future__ import absolute_import, unicode_literals

import csv
import datetime

from django.db import transaction

from . import models

@transaction.atomic
def import_rents(filename):
    '''Load the average rents per TA.
    
    For NZ, download the data from
    
    http://www.building.govt.nz/nz-housing-and-construction-quarterly-open-data
    
    IE:
    http://utilities.dbh.govt.nz/userfiles/open-data/05/geometric-mean-rents-by-ta.csv
    '''
    with open(filename, 'rb') as fileobj:
        csvreader = csv.DictReader(fileobj)
        
        last = None
        for row in csvreader:
            last = row
        
        for field in csvreader.fieldnames[2:]:
            territory_name = field
            if not territory_name.endswith(' District') and territory_name != 'Auckland':
                territory_name = territory_name + ' City'
            if territory_name == 'Tauranga District':
                territory_name = 'Tauranga City'
            elif territory_name == 'Western Bay Of Plenty District':
                territory_name = 'Western Bay of Plenty District'
            elif territory_name == "Central Hawkes Bay District":
                territory_name = "Central Hawke's Bay District"
                
            robj = models.Rents()
            robj.date = datetime.datetime.strptime(last['Date.Lodged'], '%d/%m/%Y').date()
            robj.territory = territory_name
            robj.avg_rent = float(last[field])
            robj.save()


            