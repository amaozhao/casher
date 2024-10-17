from django.urls import re_path

from task.consumer import ClientConsumer

websocket_urlpatterns = [
    re_path(r"ws/$", ClientConsumer.as_asgi()),  # 简单的路径匹配
]
