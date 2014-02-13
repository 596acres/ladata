import os

from django.conf import settings


def get_processed_data_dir():
    """
    Get the processed data directory, which can be configured by setting
    LADATA_PROCESSED_DATA_DIR in your settings. Defaults to './processed/'.
    """
    try:
        return settings.LADATA_PROCESSED_DATA_DIR
    except AttributeError:
        return os.path.join(os.path.dirname(__file__), 'processed')


def get_processed_data_file(name):
    """
    Get the processed data file with the given name.
    """
    return os.path.join(get_processed_data_dir(), name)
