"""Store Admin."""

# Django
from django.contrib import admin

# Models
from .models import Category, Product



class CategoryAdmin(admin.ModelAdmin):
    """Category admin."""
    readonly_fields = ("created", "modified")


class ProductAdmin(admin.ModelAdmin):
    """Product admin."""
    readonly_fields = ("created", "modified")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)