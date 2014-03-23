from django import template

from inplace.boundaries.templatetags.boundaries_tags import (
    BaseAllBoundariesTag,
    BaseGetBoundaryTag)

from ..models import CommunityPlanArea


class GetCommunityPlanArea(BaseGetBoundaryTag):

    def get_boundary_model(self):
        return CommunityPlanArea


class GetCommunityPlanAreas(BaseAllBoundariesTag):

    def get_value(self, context):
        return CommunityPlanArea.objects.all().order_by('label')


register = template.Library()
register.tag(GetCommunityPlanArea)
register.tag(GetCommunityPlanAreas)
