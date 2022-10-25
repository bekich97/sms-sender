from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    path('ws/sms-server/<str:app>', consumers.ChatConsumer.as_asgi())
]