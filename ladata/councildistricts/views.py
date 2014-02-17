from inplace.boundaries.views import BoundaryDetailView

from .models import CouncilDistrict


class CouncilDistrictDetailView(BoundaryDetailView):
    model = CouncilDistrict
    slug_field = 'label'
    slug_url_kwarg = 'label'
