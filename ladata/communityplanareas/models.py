# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class CommunityPlanArea(models.Model):
    objectid = models.IntegerField(null=True, blank=True)
    cpa_num = models.IntegerField(null=True, blank=True)
    name_alf = models.CharField(max_length=75, null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    shape_len = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField()
    objects = models.GeoManager()


# Auto-generated `LayerMapping` dictionary for CommunityPlanArea model
communityplanarea_mapping = {
    'objectid' : 'OBJECTID',
    'cpa_num' : 'CPA_NUM',
    'name_alf' : 'NAME_ALF',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'POLYGON',
}
