"""Urls store."""

# Django
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Views
from . import views


urlpatterns = [
    path("", views.store, name="Store"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)