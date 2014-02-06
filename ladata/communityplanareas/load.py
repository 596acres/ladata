import os

from django.contrib.gis.utils import LayerMapping

from ..load import get_processed_data_file
from .models import CommunityPlanArea, communityplanarea_mapping


def from_shapefile(strict=False, progress=True, verbose=False,
                   transaction_mode='autocommit', **kwargs):
    """
    Load community plan area data into the database from the processed
    shapefile.
    """
    shp = get_processed_data_file(os.path.join('communityplanareas', 'CPA.shp'))
    mapping = LayerMapping(CommunityPlanArea, shp, communityplanarea_mapping,
                           transform=True, transaction_mode=transaction_mode)
    mapping.save(strict=strict, progress=progress, verbose=verbose, **kwargs)


def load(**kwargs):
    from_shapefile(**kwargs)
