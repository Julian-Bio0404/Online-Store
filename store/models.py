"""Store Models."""

# Django
from django.db import models

# Utilities
from util.models import OnlineStoreModel


class Category(OnlineStoreModel):
    """Category model."""

    name = models.CharField(max_length=50)

    class Meta(OnlineStoreModel.Meta):
        """Meta options."""
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(OnlineStoreModel):
    """Product model."""

    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="store/pictures", null=True, blank=True)
    price = models.FloatField()
    available = models.BooleanField(default=True)

    class Meta(OnlineStoreModel.Meta):
        """Meta options."""
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.nombre 

