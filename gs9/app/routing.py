from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sc/<str:Group_Name>/',consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/<str:Group_Name>/', consumers.MyAsyncConsumer.as_asgi()),
]