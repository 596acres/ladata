from django.contrib.gis.db import models


class Building(models.Model):
    # This is an auto-generated Django model created by ogrinspect.
    code = models.CharField(max_length=50, null=True, blank=True)
    bld_id = models.CharField(max_length=20, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    elev = models.FloatField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    source = models.CharField(max_length=25, null=True, blank=True)
    date_field = models.CharField(max_length=4, null=True, blank=True)
    ain = models.CharField(max_length=10, null=True, blank=True)
    shape_leng = models.FloatField(null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(null=True, blank=True)
    objects = models.GeoManager()


# Auto-generated `LayerMapping` dictionary for Building model
building_mapping = {
    'code' : 'CODE',
    'bld_id' : 'BLD_ID',
    'height' : 'HEIGHT',
    'elev' : 'ELEV',
    'area' : 'AREA',
    'source' : 'SOURCE',
    'date_field' : 'DATE_',
    'ain' : 'AIN',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'POLYGON',
}
