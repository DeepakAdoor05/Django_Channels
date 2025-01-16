# It's same as urls.py connecting with views
# Here routing.py connecting with consumers  
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sc/',consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/',consumers.MyASyncConsumer.as_asgi()),
]