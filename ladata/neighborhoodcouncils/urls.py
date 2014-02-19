from django.conf.urls import patterns, url

from .views import NeighborhoodCouncilDetailView


urlpatterns = patterns('',

    url(r'^(?P<label>[^/]+)/geojson/$', NeighborhoodCouncilDetailView.as_view(),
        name='neighborhoodcouncil_details_geojson'),

)
