from django.contrib.gis.db import models


class Parcel(models.Model):
    """
    A parcel as defined by the Los Angeles County Assessor:

        http://assessor.lacounty.gov/extranet/outsidesales/gisdata.aspx
    """
    # This is an auto-generated Django model module created by ogrinspect.
    objectid = models.IntegerField(null=True, blank=True)
    assrdata_m = models.FloatField(null=True, blank=True)
    perimeter = models.FloatField(null=True, blank=True)
    phase = models.CharField(max_length=2, null=True, blank=True)
    lot = models.CharField(max_length=4, null=True, blank=True)
    unit = models.CharField(max_length=4, null=True, blank=True)
    moved = models.CharField(max_length=1, null=True, blank=True)
    tra = models.CharField(max_length=6, null=True, blank=True)
    pcltype = models.CharField(max_length=2, null=True, blank=True)
    subdtype = models.CharField(max_length=2, null=True, blank=True)
    tract = models.CharField(max_length=20, null=True, blank=True)
    usecode = models.CharField(max_length=4, null=True, blank=True)
    block = models.CharField(max_length=5, null=True, blank=True)
    udate = models.DateField(null=True, blank=True)
    editorname = models.CharField(max_length=35, null=True, blank=True)
    parcel_typ = models.IntegerField(null=True, blank=True)
    unit_no = models.CharField(max_length=25, null=True, blank=True)
    pm_ref = models.CharField(max_length=15, null=True, blank=True)
    tot_units = models.IntegerField(null=True, blank=True)
    ain = models.CharField(max_length=10, null=True, blank=True)
    globalid = models.CharField(max_length=38, null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    shape_len = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(null=True, blank=True)
    local_roll = models.ForeignKey('localroll.LocalRollAEntry', null=True,
                                   blank=True)
    objects = models.GeoManager()

    def _street_address(self):
        if not self.local_roll:
            return None
        street_address = self.local_roll.street_address
        if street_address == '0':
            street_address = None
        return street_address
    street_address = property(_street_address)

    def _city(self):
        if not self.local_roll:
            return None
        return self.local_roll.city
    city = property(_city)

    def _state(self):
        if not self.local_roll:
            return None
        return self.local_roll.state
    state = property(_state)

    def _zip_code(self):
        if not self.local_roll:
            return None
        return self.local_roll.zip_code
    zip_code = property(_zip_code)


# Auto-generated `LayerMapping` dictionary for Parcel model
parcel_mapping = {
    'objectid' : 'OBJECTID',
    'assrdata_m' : 'ASSRDATA_M',
    'perimeter' : 'PERIMETER',
    'phase' : 'PHASE',
    'lot' : 'LOT',
    'unit' : 'UNIT',
    'moved' : 'MOVED',
    'tra' : 'TRA',
    'pcltype' : 'PCLTYPE',
    'subdtype' : 'SUBDTYPE',
    'tract' : 'TRACT',
    'usecode' : 'USECODE',
    'block' : 'BLOCK',
    'udate' : 'UDATE',
    'editorname' : 'EDITORNAME',
    'parcel_typ' : 'PARCEL_TYP',
    'unit_no' : 'UNIT_NO',
    'pm_ref' : 'PM_REF',
    'tot_units' : 'TOT_UNITS',
    'ain' : 'AIN',
    'globalid' : 'GlobalID',
    'shape_area' : 'SHAPE_area',
    'shape_len' : 'SHAPE_len',
    'geom' : 'POLYGON',
}
