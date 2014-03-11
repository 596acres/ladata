from django.db import models


class TransmissionLine(models.Model):
    apn = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    type = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    ownership_type = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )

    # Was Field8 in original database
    agency = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    # Was Field9 in original database
    city = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    tran_line_no = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    # Was Field4 in original database
    notes = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    parcel = models.ForeignKey('parcels.Parcel', null=True, blank=True)


# Manually made, but meant to do a similar thing to GeoDjango mappings
transmissionline_mapping = {
    'APN': 'apn',
    'TYPE': 'type',
    'ownership type': 'ownership_type',
    'Field8': 'agency',
    'Field9': 'city',
    'Tran Line no': 'tran_line_no',
    'Field4': 'notes',
}
