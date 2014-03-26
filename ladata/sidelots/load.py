import csv
import os

from ..load import get_processed_data_file
from ..parcels.models import Parcel
from .models import SideLot, sidelot_mapping


def from_csv(filename=None, progress=True, skip_existing=True, verbose=False,
             only_for_existing_parcels=True, **kwargs):
    """
    Load parcel data into the database from the processed csv.
    """
    if not filename:
        filename = get_processed_data_file(os.path.join('sidelots',
                                                        'sidelots.csv'))

    def header_to_field(header):
        return sidelot_mapping.get(header, None)

    def clean_kwarg_boolean(name, **kwargs):
        return kwargs.get(name, None) == '1'

    def clean_kwarg_int(name, **kwargs):
        try:
            return int(kwargs[name])
        except Exception:
            return None

    def clean_kwarg_float(name, **kwargs):
        try:
            return float(kwargs[name])
        except Exception:
            return None

    def clean_kwargs(**kwargs):
        kwargs['cnt_apn'] = clean_kwarg_int('cnt_apn', **kwargs)
        kwargs['land_sqft'] = clean_kwarg_float('land_sqft', **kwargs)
        kwargs['access'] = clean_kwarg_boolean('access', **kwargs)
        kwargs['field_checked'] = clean_kwarg_boolean('field_checked', **kwargs)
        kwargs['phase'] = clean_kwarg_int('phase', **kwargs)
        return kwargs

    count = 0
    for row in csv.DictReader(open(filename, 'r')):
        apn = row['APN']
        count += 1
        if count % 500 == 0 and progress:
            print count
        if verbose:
            print apn

        try:
            parcel = Parcel.objects.get(ain=apn)
        except (Parcel.MultipleObjectsReturned, Parcel.DoesNotExist):
            parcel = None
            if only_for_existing_parcels:
                print 'not adding for NO. %s, no parcel' % row['NO.']
                continue

        # Get or create
        try:
            sidelot = SideLot.objects.get(apn=apn)
            if skip_existing:
                continue
        except SideLot.DoesNotExist:
            kwargs = dict([(header_to_field(k), v) for k, v in row.items()])
            kwargs = dict([(k, v) for k, v in kwargs.items() if k is not None])
            sidelot = SideLot(**clean_kwargs(**kwargs))

        # Link with Parcel if exists
        if parcel:
            sidelot.parcel = parcel

        sidelot.save()


def load(**kwargs):
    from_csv(**kwargs)
