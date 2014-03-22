from django.contrib.gis.db import models

from inplace.boundaries.models import BaseBoundary


class ZoningDistrict(BaseBoundary):
    objectid = models.IntegerField(null=True, blank=True)
    zone_cmplt = models.CharField(max_length=30, null=True, blank=True)
    zone_under = models.CharField(max_length=30, null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    shape_len = models.FloatField(null=True, blank=True)
    zone_class = models.CharField(max_length=8, null=True, blank=True)
    zone_code = models.IntegerField(null=True, blank=True)
    objects = models.GeoManager()


zoningdistrict_mapping = {
    'label' : 'ZONE_CLASS',
    'objectid' : 'OBJECTID',
    'zone_cmplt' : 'ZONE_CMPLT',
    'zone_under' : 'ZONE_UNDER',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'zone_class' : 'ZONE_CLASS',
    'zone_code' : 'ZONE_CODE',
    'geometry' : 'POLYGON',
}
