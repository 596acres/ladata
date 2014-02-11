import os

from django.contrib.gis.utils import LayerMapping

from ..load import get_processed_data_file
from .models import Parcel, parcel_mapping


def from_shapefile(council_district=None, strict=False, progress=True,
                   verbose=False, transaction_mode='autocommit', **kwargs):
    """
    Load parcel data into the database from the processed shapefile.
    """
    # Using transaction_mode=autocommit because otherwise LayerMapping gets
    # stuck on a feature and can't commit anything
    filename = os.path.join('parcels', 'split',
                            'council_district_%s.shp' % council_district)
    parcel_shp = get_processed_data_file(filename)
    mapping = LayerMapping(Parcel, parcel_shp, parcel_mapping, transform=True,
                           transaction_mode=transaction_mode)
    mapping.save(strict=strict, progress=progress, verbose=verbose, **kwargs)


def load(**kwargs):
    from_shapefile(**kwargs)
