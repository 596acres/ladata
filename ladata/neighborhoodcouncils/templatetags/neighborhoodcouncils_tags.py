from django import template

from inplace.boundaries.templatetags.boundaries_tags import (
    BaseAllBoundariesTag,
    BaseGetBoundaryTag)

from ..models import NeighborhoodCouncil


class GetNeighborhoodCouncil(BaseGetBoundaryTag):

    def get_boundary_model(self):
        return NeighborhoodCouncil


class GetNeighborhoodCouncils(BaseAllBoundariesTag):

    def get_value(self, context):
        return NeighborhoodCouncil.objects.order_by('label')


register = template.Library()
register.tag(GetNeighborhoodCouncil)
register.tag(GetNeighborhoodCouncils)
