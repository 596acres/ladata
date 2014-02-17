# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

from inplace.boundaries.models import BaseBoundary


class CouncilDistrict(BaseBoundary):
    cdmember = models.CharField(max_length=30, null=True, blank=True)
    sq_mi = models.CharField(max_length=15, null=True, blank=True)
    shadesym = models.IntegerField(null=True, blank=True)
    revised = models.CharField(max_length=20, null=True, blank=True)
    comments = models.CharField(max_length=100, null=True, blank=True)
    objects = models.GeoManager()


# Auto-generated `LayerMapping` dictionary for CouncilDistrict model
councildistrict_mapping = {
    'cdmember' : 'CDMEMBER',
    'label' : 'DISTRICT',
    'sq_mi' : 'SQ_MI',
    'shadesym' : 'SHADESYM',
    'revised' : 'REVISED',
    'comments' : 'COMMENTS',
    'geometry' : 'POLYGON',
}
