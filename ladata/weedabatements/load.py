import csv
import os

from ..load import get_processed_data_file
from ..parcels.models import Parcel
from .models import WeedAbatement, weedabatement_mapping


def from_csv(progress=True, skip_existing=True, verbose=False,
             only_for_existing_parcels=True, **kwargs):
    """
    Load parcel data into the database from the processed csv.
    """
    input_file = get_processed_data_file(os.path.join('weedabatements',
                                                      'weedabatements.csv'))

    def header_to_field(header):
        return weedabatement_mapping.get(header, None)

    def clean_kwargs(**kwargs):
        kwargs['no_clean'] = (kwargs.get('no_clean', None) == '1')
        kwargs['vacant'] = (kwargs.get('vacant', None) == '1')
        try:
            kwargs['lien'] = float(kwargs['lien'])
        except Exception:
            kwargs['lien'] = None
        return kwargs

    count = 0
    for row in csv.DictReader(open(input_file, 'r')):
        ain = row['AIN']
        count += 1
        if count % 500 == 0 and progress:
            print count
        if verbose:
            print ain

        try:
            parcel = Parcel.objects.get(ain=ain)
        except (Parcel.MultipleObjectsReturned, Parcel.DoesNotExist):
            parcel = None
            if only_for_existing_parcels:
                continue

        # Get or create
        try:
            weed_abatement = WeedAbatement.objects.get(ain=ain)
            if skip_existing:
                continue
        except WeedAbatement.DoesNotExist:
            kwargs = dict([(header_to_field(k), v) for k, v in row.items()])
            kwargs = dict([(k, v) for k, v in kwargs.items() if k is not None])
            weed_abatement = WeedAbatement(**clean_kwargs(**kwargs))

        # Link with Parcel if exists
        if parcel:
            weed_abatement.parcel = parcel

        weed_abatement.save()


def load(**kwargs):
    from_csv(**kwargs)
