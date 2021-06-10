"""Services Admin."""

# Django
from django.contrib import admin

# Models
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    """Service model admin."""

    readonly_fields = ("created", "modified")


admin.site.register(Service, ServiceAdmin)