"""Contact urls."""

# Django
from django.urls import path

# Views
from . import views


urlpatterns = [
    path("", views.contact, name="Contact"),
]