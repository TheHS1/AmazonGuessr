from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getDBData", views.getDBData, name="getDBData"),
]
