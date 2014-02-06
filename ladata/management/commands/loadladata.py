from importlib import import_module
import traceback

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = 'dataset_name'
    help = 'Loads LA data (addresses, buildings, parcels, ...)'

    datasets = {
        # name -> module
        'buildings': 'buildings',
        'communityplanareas': 'communityplanareas',
        'councildistricts': 'councildistricts',
        'localroll': 'localroll',
        'parcels': 'parcels',
        'protectedareas': 'protectedareas',
    }

    def handle(self, dataset_name, *args, **options):
        try:
            load_module = import_module('ladata.%s.load' % self.datasets[dataset_name])
            load_module.load()
        except KeyError:
            traceback.print_exc()
            raise CommandError('Could not find dataset %s' % dataset_name)
        except Exception:
            traceback.print_exc()
            raise CommandError('There was a problem loading data')
