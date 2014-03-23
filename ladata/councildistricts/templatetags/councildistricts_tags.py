from django import template

from inplace.boundaries.templatetags.boundaries_tags import (
    BaseAllBoundariesTag,
    BaseGetBoundaryTag)

from ..models import CouncilDistrict


class GetCouncilDistrict(BaseGetBoundaryTag):

    def get_boundary_model(self):
        return CouncilDistrict


class GetCouncilDistricts(BaseAllBoundariesTag):

    def get_value(self, context):
        return CouncilDistrict.objects.extra(
            select={
                'labelinteger': 'CAST(label AS INTEGER)',
            }
        ).order_by('labelinteger')


register = template.Library()
register.tag(GetCouncilDistrict)
register.tag(GetCouncilDistricts)
