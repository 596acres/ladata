import os

from django.contrib.gis.utils import LayerMapping

from ..load import get_processed_data_file
from .models import Building, building_mapping


def from_shapefile(strict=False, progress=True, verbose=False,
                   transaction_mode='autocommit', **kwargs):
    """
    Load building data into the database from the processed shapefile.
    """
    # Using transaction_mode=autocommit because otherwise LayerMapping gets
    # stuck on a feature and can't commit anything
    shp = get_processed_data_file(os.path.join('buildings',
                                               'lariac_buildings_2008.shp'))
    mapping = LayerMapping(Building, shp, building_mapping, transform=True,
                           transaction_mode=transaction_mode)
    mapping.save(strict=strict, progress=progress, verbose=verbose, **kwargs)


def load(**kwargs):
    from_shapefile(**kwargs)
