"""Urls store."""

# Django
from django.urls import path

# Views
from . import views


urlpatterns = [
    path("", views.store, name="Store"),
]