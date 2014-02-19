from inplace.boundaries.views import BoundaryDetailView

from .models import NeighborhoodCouncil


class NeighborhoodCouncilDetailView(BoundaryDetailView):
    model = NeighborhoodCouncil
    slug_field = 'label'
    slug_url_kwarg = 'label'
