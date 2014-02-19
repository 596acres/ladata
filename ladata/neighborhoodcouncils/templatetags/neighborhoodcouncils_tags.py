from django import template

from inplace.boundaries.templatetags.boundaries_tags import BaseAllBoundariesTag

from ..models import NeighborhoodCouncil


class GetNeighborhoodCouncils(BaseAllBoundariesTag):

    def get_value(self, context):
        return NeighborhoodCouncil.objects.order_by('label')


register = template.Library()
register.tag(GetNeighborhoodCouncils)
