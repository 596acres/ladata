import os

from django.contrib.gis.utils import LayerMapping

from ..load import get_processed_data_file
from .models import NeighborhoodCouncil, neighborhoodcouncil_mapping


def from_shapefile(strict=False, progress=True, verbose=False,
                   transaction_mode='autocommit',
                   filename='neighborhoodcouncils.shp', **kwargs):
    """
    Load neighborhood council data into the database from the processed
    shapefile.
    """
    shp = get_processed_data_file(os.path.join('neighborhoodcouncils', filename))
    mapping = LayerMapping(NeighborhoodCouncil, shp, neighborhoodcouncil_mapping,
                           transform=True, transaction_mode=transaction_mode)
    mapping.save(strict=strict, progress=progress, verbose=verbose, **kwargs)


def load(**kwargs):
    from_shapefile(**kwargs)
