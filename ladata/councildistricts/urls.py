from django.conf.urls import patterns, url

from .views import CouncilDistrictDetailView


urlpatterns = patterns('',

    url(r'^(?P<label>[^/]+)/geojson/$', CouncilDistrictDetailView.as_view(),
        name='councildistrict_details_geojson'),

)
