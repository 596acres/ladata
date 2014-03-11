import csv
import os

from ..load import get_processed_data_file
from ..parcels.models import Parcel
from .models import TransmissionLine, transmissionline_mapping


def from_csv(progress=True, skip_existing=True, verbose=False,
             only_for_existing_parcels=True, **kwargs):
    """
    Load parcel data into the database from the processed csv.
    """
    input_file = get_processed_data_file(os.path.join('transmissionlines',
                                                      'transmissionlines.csv'))

    def header_to_field(header):
        return transmissionline_mapping.get(header, None)

    count = 0
    for row in csv.DictReader(open(input_file, 'r')):
        ain = row['APN']
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
            transmission_line = TransmissionLine.objects.get(apn=ain)
            if skip_existing:
                continue
        except TransmissionLine.DoesNotExist:
            kwargs = dict([(header_to_field(k), v) for k, v in row.items()])
            kwargs = dict([(k, v) for k, v in kwargs.items() if k is not None])
            transmission_line = TransmissionLine(**kwargs)

        # Link with Parcel if exists
        if parcel:
            transmission_line.parcel = parcel

        transmission_line.save()


def load(**kwargs):
    from_csv(**kwargs)
