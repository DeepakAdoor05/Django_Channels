from django.urls import path
from . import views

urlpatterns = [
    path('<str:group_name>/',views.index), # Passing the group name from url to views
]
