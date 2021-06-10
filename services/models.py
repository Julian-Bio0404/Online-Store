"""Services Models."""

# Django
from django.db import models

# Utilities
from util.models import OnlineStoreModel


class Service(OnlineStoreModel):
    """Service model."""

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="services")

    class Meta(OnlineStoreModel.Meta):
        """Meta options."""
        verbose_name = "service"
        verbose_name_plural = "services"

    def __str__(self):
        """Return tittle´s service"""
        return self.title



