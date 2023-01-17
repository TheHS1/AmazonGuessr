from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("processGame", views.processGame, name="processGame"),
    path("getHint", views.getHint, name="getHint"),
]
