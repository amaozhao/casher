from django.urls import re_path

from socketer.consumer import Consumer

websocket_urlpatterns = [
    re_path(r"ws/(?P<clinet_id>\w+)/$", Consumer.as_asgi()),
]