from collections import OrderedDict

from django.core.management.base import BaseCommand

from ...buildings.models import Building
from ...communityplanareas.models import CommunityPlanArea
from ...councildistricts.models import CouncilDistrict
from ...localroll.models import LocalRollAEntry
from ...parcels.models import Parcel
from ...protectedareas.models import ProtectedArea


class Command(BaseCommand):
    help = 'Get LA data status'

    datasets = OrderedDict([
        # name -> model
        ('buildings', Building),
        ('communityplanareas', CommunityPlanArea),
        ('councildistricts', CouncilDistrict),
        ('localroll', LocalRollAEntry),
        ('parcels', Parcel),
        ('protectedareas', ProtectedArea),
    ])

    def handle(self, *args, **options):
        print 'LA data status'
        print '==============\n'
        for dataset_name, model in self.datasets.items():
            print '%s: %d' % (dataset_name, model.objects.count())
