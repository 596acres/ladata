from django import template

from inplace.boundaries.templatetags.boundaries_tags import BaseAllBoundariesTag

from ..models import CouncilDistrict


class GetCouncilDistricts(BaseAllBoundariesTag):

    def get_value(self, context):
        return CouncilDistrict.objects.extra(
            select={
                'labelinteger': 'CAST(label AS INTEGER)',
            }
        ).order_by('labelinteger')


register = template.Library()
register.tag(GetCouncilDistricts)
