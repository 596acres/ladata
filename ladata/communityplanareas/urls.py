from django.conf.urls import patterns, url

from .views import CommunityPlanAreaDetailView


urlpatterns = patterns('',

    url(r'^(?P<label>[^/]+)/geojson/$', CommunityPlanAreaDetailView.as_view(),
        name='communityplanarea_details_geojson'),

)
