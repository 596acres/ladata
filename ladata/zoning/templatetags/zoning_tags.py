from collections import OrderedDict

from django import template

from classytags.core import Options
from classytags.arguments import Argument
from classytags.helpers import AsTag


class GetZoningClasses(AsTag):

    options = Options(
        'as',
        Argument('varname', resolve=False, required=False),
    )

    def get_value(self, context):
        return OrderedDict((
            ('Single-Family Residential', [
                'R1',
                'RE',
                'RS',
                'RU',
                'RW1',
                'RZ',
            ]),
            ('Multi-Family Residential', [
                'R2',
                'R4',
                'RD',
                'RAS',
                'RS',
                'RW2',
            ]),
            ('Commercial', [
                'CR',
                'C1',
                'C2',
                'C4',
                'CW',
                'LASED',
                'USC',
            ]),
            ('Industrial', [
                'CM',
                'MR',
                'WC',
                'CCS',
                'UV',
                'UI',
                'UC',
                'M1',
                'M2',
                'LAX',
                'M3',
                'SL',
            ]),
            ('Open Space', [
                'OS',
                'GW',
            ]),
            ('Agriculture', [
                'A',
                'RA',
            ]),
            ('Parking', [
                'P',
                'PB',
            ]),
            ('Public Facilities', [
                'PF',
            ]),
            ('Hillside', [
                'HILLSIDE',
            ]),
        ))


register = template.Library()
register.tag(GetZoningClasses)
