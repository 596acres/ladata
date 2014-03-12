from django.db import models


class WeedAbatement(models.Model):
    ain = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    no_clean = models.NullBooleanField(
        null=True,
        blank=True,
    )

    lien = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True,
        blank=True,
    )

    vacant = models.NullBooleanField(
        null=True,
        blank=True,
    )

    parcel = models.ForeignKey('parcels.Parcel', null=True, blank=True)

    added = models.DateTimeField(auto_now=True)


# Manually made, but meant to do a similar thing to GeoDjango mappings
weedabatement_mapping = {
    'AIN': 'ain',
    'NOCLEAN': 'no_clean',
    'LIEN': 'lien',
    'VACANT': 'vacant',
}
