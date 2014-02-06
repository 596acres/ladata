from django.contrib.gis.db import models

class ProtectedArea(models.Model):
    # This is an auto-generated Django model module created by ogrinspect.
    agncy_name = models.CharField(max_length=250, null=True, blank=True)
    unit_name = models.CharField(max_length=200, null=True, blank=True)
    access_typ = models.CharField(max_length=17, null=True, blank=True)
    county = models.CharField(max_length=15, null=True, blank=True)
    agncy_lev = models.CharField(max_length=16, null=True, blank=True)
    agncy_web = models.CharField(max_length=100, null=True, blank=True)
    layer = models.CharField(max_length=45, null=True, blank=True)
    mng_agncy = models.CharField(max_length=100, null=True, blank=True)
    label_name = models.CharField(max_length=100, null=True, blank=True)
    own_type = models.CharField(max_length=8, null=True, blank=True)
    unit_id = models.IntegerField(null=True, blank=True)
    superunit = models.CharField(max_length=100, null=True, blank=True)
    agncy_id = models.IntegerField(null=True, blank=True)
    mng_ag_id = models.IntegerField(null=True, blank=True)
    gis_acres = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField()
    objects = models.GeoManager()


# Auto-generated `LayerMapping` dictionary for ProtectedArea model
protectedarea_mapping = {
    'agncy_name' : 'AGNCY_NAME',
    'unit_name' : 'UNIT_NAME',
    'access_typ' : 'ACCESS_TYP',
    'county' : 'COUNTY',
    'agncy_lev' : 'AGNCY_LEV',
    'agncy_web' : 'AGNCY_WEB',
    'layer' : 'LAYER',
    'mng_agncy' : 'MNG_AGNCY',
    'label_name' : 'LABEL_NAME',
    'own_type' : 'OWN_TYPE',
    'unit_id' : 'UNIT_ID',
    'superunit' : 'SUPERUNIT',
    'agncy_id' : 'AGNCY_ID',
    'mng_ag_id' : 'MNG_AG_ID',
    'gis_acres' : 'GIS_ACRES',
    'geom' : 'POLYGON',
}
