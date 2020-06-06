from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/data/(?P<id>\w+)/$', consumers.DataConsumer),
    re_path(r'ws/connection/(?P<connection>\w+)/$', consumers.ConnectionConsumer),
    re_path(r'ws/fleet/(?P<fleet_id>\w+)/(?P<id>\w+)/$', consumers.FleetConsumer )
]