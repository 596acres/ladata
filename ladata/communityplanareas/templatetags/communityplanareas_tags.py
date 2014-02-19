from django import template

from inplace.boundaries.templatetags.boundaries_tags import BaseAllBoundariesTag

from ..models import CommunityPlanArea


class GetCommunityPlanAreas(BaseAllBoundariesTag):

    def get_value(self, context):
        return CommunityPlanArea.objects.all().order_by('label')


register = template.Library()
register.tag(GetCommunityPlanAreas)
