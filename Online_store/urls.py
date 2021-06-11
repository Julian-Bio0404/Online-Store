"""Online_store URL Configuration."""

# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("online_storeapp.urls")),
    path('store/', include("store.urls")),
    path('carro/', include("carrito.urls")),
    path('blog/', include("blog.urls")),
    path("services/", include("services.urls")),
    path('contact/', include("contact.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)