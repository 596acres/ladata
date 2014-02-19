from inplace.boundaries.views import BoundaryDetailView

from .models import CommunityPlanArea


class CommunityPlanAreaDetailView(BoundaryDetailView):
    model = CommunityPlanArea
    slug_field = 'label'
    slug_url_kwarg = 'label'
