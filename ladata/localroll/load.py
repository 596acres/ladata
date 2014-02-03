import csv
import os

from ..load import get_processed_data_file
from ..parcels.models import Parcel
from .models import LocalRollAEntry


def from_csv(progress=True, skip_existing=True, start=1, verbose=False,
             **kwargs):
    """
    Load parcel data into the database from the processed csv.
    """
    localroll_file = get_processed_data_file(os.path.join('localroll',
                                                          'LocalRollA.csv'))
    def header_to_field(header):
        field = header.strip().lower().replace(' ', '_')
        return field.replace('1st', 'first').replace('2nd', 'second')

    count = 0
    for row in csv.DictReader(open(localroll_file, 'r')):
        ain = row['AIN']
        count += 1
        if count < start:
            continue
        if count % 1000 == 0 and progress:
            print count
        if verbose:
            print ain

        # Get or create LocalRollAEntry
        try:
            entry = LocalRollAEntry.objects.get(ain=ain)
            if skip_existing:
                continue
        except LocalRollAEntry.DoesNotExist:
            kwargs = dict([(header_to_field(k), v) for k, v in row.items()])
            entry = LocalRollAEntry(**kwargs)
            entry.save()

        # Link with Parcel if exists
        try:
            parcel = Parcel.objects.get(ain=ain)
            parcel.local_roll = entry
            parcel.save()
        except Parcel.MultipleObjectsReturned:
            pass
        except Parcel.DoesNotExist:
            pass


def load(**kwargs):
    from_csv(**kwargs)
