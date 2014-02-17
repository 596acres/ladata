from django import template

from inplace.boundaries.templatetags.boundaries_tags import BaseAllBoundariesTag

from ..models import CouncilDistrict


class GetCouncilDistricts(BaseAllBoundariesTag):

    def get_value(self, context):
        return CouncilDistrict.objects.all().order_by('label')


register = template.Library()
register.tag(GetCouncilDistricts)
