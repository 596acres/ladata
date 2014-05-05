import json
import geojson

from django.contrib.gis.geos import Polygon

from inplace.views import GeoJSONListView
from .models import Parcel


class GeoJSONPolygonView(GeoJSONListView):
    model = Parcel

    def get_feature(self, parcel):
        return geojson.Feature(
            parcel.pk,
            geometry=json.loads(parcel.geojson),
            properties=self.get_properties(parcel),
        )

    def get_properties(self, parcel):
        return {
            'address': parcel.street_address,
        }

    def get_queryset(self):
        try:
            bbox = Polygon.from_bbox(self.request.GET['bbox'].split(','))
            return super(GeoJSONPolygonView, self).get_queryset().filter(
                geom__intersects=bbox,
            ).select_related('local_roll').geojson(precision=6)
        except KeyError:
            return Parcel.objects.none()

