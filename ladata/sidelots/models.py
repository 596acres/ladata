from django.db import models


class SideLot(models.Model):
	no = models.CharField(max_length=8, null=True, blank=True)
	cd = models.CharField(max_length=4, null=True, blank=True)
	apn = models.CharField(max_length=20, null=True, blank=True)
	cnt_apn = models.IntegerField(null=True, blank=True)
	address = models.CharField(max_length=100, null=True, blank=True)
	intersection = models.CharField(max_length=100, null=True, blank=True)
	land_sqft = models.FloatField(null=True, blank=True)
	access = models.NullBooleanField(null=True, blank=True)
	zoning = models.CharField(max_length=11, null=True, blank=True)
	tbpg = models.CharField(max_length=6, null=True, blank=True)
	topography = models.CharField(max_length=8, null=True, blank=True)
	type = models.CharField(max_length=4, null=True, blank=True)
	status = models.CharField(max_length=80, null=True, blank=True)
	source_of_funds = models.CharField(max_length=32, null=True, blank=True)
	est_price_per_sqft_3_08 = models.CharField(max_length=7, null=True,
                                               blank=True)
	formula_3_08 = models.CharField(max_length=7, null=True, blank=True)
	class_c_3_08 = models.CharField(max_length=10, null=True, blank=True)
	remarks_by_appraisal = models.CharField(max_length=50, null=True,
                                            blank=True)
	field_checked = models.NullBooleanField(null=True, blank=True)
	phase = models.IntegerField(null=True, blank=True)
	synopsis_comments = models.TextField(null=True, blank=True)
	parcel = models.ForeignKey('parcels.Parcel', null=True, blank=True)


# Manually made, but meant to do a similar thing to GeoDjango mappings
sidelot_mapping = {
    'NO.': 'no',
    'CD': 'cd',
    'APN': 'apn',
    'Cnt_APN': 'cnt_apn',
    'ADDRESS': 'address',
    'INTERSECTION': 'intersection',
    '"LAND ""SQFT"""': 'land_sqft',
    'ACCESS': 'access',
    'ZONING': 'zoning',
    'TBpg': 'tbpg',
    'Topography': 'topography',
    'TYPE': 'type',
    'STATUS': 'status',
    'SOURCE OF FUNDS': 'source_of_funds',
    'est $/SF 3/08': 'est_price_per_sqft_3_08',
    'Formula  3/08': 'formula_3_08',
    '"CLASS ""C"" 3/08"': 'class_c_3_08',
    'Remarks by Appraisal': 'remarks_by_appraisal',
    'Field_Checked': 'field_checked',
    'PHASE': 'phase',
    'SYNOPSIS COMMENTS': 'synopsis_comments',
}
