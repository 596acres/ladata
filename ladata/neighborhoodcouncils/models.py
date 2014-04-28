# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

from inplace.boundaries.models import BaseBoundary


class NeighborhoodCouncil(BaseBoundary):
    area = models.FloatField(null=True, blank=True)
    perimeter = models.FloatField(null=True, blank=True)
    cname1 = models.CharField(max_length=45, null=True, blank=True)
    cphone1 = models.CharField(max_length=45, null=True, blank=True)
    cemail1 = models.CharField(max_length=45, null=True, blank=True)
    ctitle1 = models.CharField(max_length=45, null=True, blank=True)
    cname2 = models.CharField(max_length=45, null=True, blank=True)
    cphone2 = models.CharField(max_length=45, null=True, blank=True)
    cemail2 = models.CharField(max_length=45, null=True, blank=True)
    ctitle2 = models.CharField(max_length=45, null=True, blank=True)
    cname3 = models.CharField(max_length=45, null=True, blank=True)
    cphone3 = models.CharField(max_length=45, null=True, blank=True)
    cemail3 = models.CharField(max_length=45, null=True, blank=True)
    ctitle3 = models.CharField(max_length=45, null=True, blank=True)
    cname4 = models.CharField(max_length=45, null=True, blank=True)
    cphone4 = models.CharField(max_length=45, null=True, blank=True)
    cemail4 = models.CharField(max_length=45, null=True, blank=True)
    ctitle4 = models.CharField(max_length=45, null=True, blank=True)
    cname5 = models.CharField(max_length=45, null=True, blank=True)
    cphone5 = models.CharField(max_length=45, null=True, blank=True)
    cemail5 = models.CharField(max_length=45, null=True, blank=True)
    ctitle5 = models.CharField(max_length=45, null=True, blank=True)
    cname6 = models.CharField(max_length=45, null=True, blank=True)
    cphone6 = models.CharField(max_length=45, null=True, blank=True)
    cemail6 = models.CharField(max_length=45, null=True, blank=True)
    ctitle6 = models.CharField(max_length=45, null=True, blank=True)
    cname7 = models.CharField(max_length=45, null=True, blank=True)
    cphone7 = models.CharField(max_length=45, null=True, blank=True)
    cemail7 = models.CharField(max_length=45, null=True, blank=True)
    ctitle7 = models.CharField(max_length=45, null=True, blank=True)
    waddress = models.CharField(max_length=45, null=True, blank=True)
    oaddr = models.CharField(max_length=50, null=True, blank=True)
    ocity = models.CharField(max_length=50, null=True, blank=True)
    ozip = models.CharField(max_length=45, null=True, blank=True)
    otel = models.CharField(max_length=45, null=True, blank=True)
    ofax = models.CharField(max_length=45, null=True, blank=True)
    dname1 = models.CharField(max_length=45, null=True, blank=True)
    dphone1 = models.CharField(max_length=45, null=True, blank=True)
    dname2 = models.CharField(max_length=50, null=True, blank=True)
    dphone2 = models.CharField(max_length=50, null=True, blank=True)
    dwebsite = models.CharField(max_length=75, null=True, blank=True)
    demail = models.CharField(max_length=45, null=True, blank=True)
    dphone = models.CharField(max_length=45, null=True, blank=True)
    oid_field = models.IntegerField(null=True, blank=True)
    nc_id = models.FloatField(null=True, blank=True)
    certified = models.DateField(null=True, blank=True)
    newsqmile = models.FloatField(null=True, blank=True)
    objects = models.GeoManager()

    def fix_label_capitalization(self):
        return self.label.title().replace('Nc', 'NC').replace('Ndc', 'NDC')


# Auto-generated `LayerMapping` dictionary for NeighborhoodCouncil model
neighborhoodcouncil_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'label' : 'NAME',
    'cname1' : 'CNAME1',
    'cphone1' : 'CPHONE1',
    'cemail1' : 'CEMAIL1',
    'ctitle1' : 'CTITLE1',
    'cname2' : 'CNAME2',
    'cphone2' : 'CPHONE2',
    'cemail2' : 'CEMAIL2',
    'ctitle2' : 'CTITLE2',
    'cname3' : 'CNAME3',
    'cphone3' : 'CPHONE3',
    'cemail3' : 'CEMAIL3',
    'ctitle3' : 'CTITLE3',
    'cname4' : 'CNAME4',
    'cphone4' : 'CPHONE4',
    'cemail4' : 'CEMAIL4',
    'ctitle4' : 'CTITLE4',
    'cname5' : 'CNAME5',
    'cphone5' : 'CPHONE5',
    'cemail5' : 'CEMAIL5',
    'ctitle5' : 'CTITLE5',
    'cname6' : 'CNAME6',
    'cphone6' : 'CPHONE6',
    'cemail6' : 'CEMAIL6',
    'ctitle6' : 'CTITLE6',
    'cname7' : 'CNAME7',
    'cphone7' : 'CPHONE7',
    'cemail7' : 'CEMAIL7',
    'ctitle7' : 'CTITLE7',
    'waddress' : 'WADDRESS',
    'oaddr' : 'OADDR',
    'ocity' : 'OCITY',
    'ozip' : 'OZIP',
    'otel' : 'OTEL',
    'ofax' : 'OFAX',
    'dname1' : 'DNAME1',
    'dphone1' : 'DPHONE1',
    'dname2' : 'DNAME2',
    'dphone2' : 'DPHONE2',
    'dwebsite' : 'DWEBSITE',
    'demail' : 'DEMAIL',
    'dphone' : 'DPHONE',
    'oid_field' : 'OID_',
    'nc_id' : 'NC_ID',
    'certified' : 'CERTIFIED',
    'newsqmile' : 'newsqmile',
    'geometry' : 'POLYGON',
}
