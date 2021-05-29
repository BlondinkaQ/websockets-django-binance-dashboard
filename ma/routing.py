from django.urls import path

from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/change/', WSConsumer.as_asgi())

]