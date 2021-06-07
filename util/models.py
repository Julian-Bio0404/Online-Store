"""Utilities Model."""

# Django
from django.db import models


class OnlineStoreModel(models.Model):
    """Abstract Model."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta options."""
        abstract = True
        ordering = ["-created", "-modified"]
