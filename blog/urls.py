"""URL´s blog."""

# Django
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# views
from . import views

urlpatterns = [
    path("", views.blog, name="Blog"),
    path("categoria/<int:categoria_id>/", views.category, name="Categoria")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)