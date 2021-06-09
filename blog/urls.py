"""URL´s blog."""

# Django
from django.urls import path
from django.conf import settings

# views
from . import views

urlpatterns = [
    path("", views.blog, name="Blog"),
    path("categoria/<int:categoria_id>/", views.category, name="Categoria")
]