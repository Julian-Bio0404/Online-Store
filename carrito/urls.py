"""Urls carrito."""

# Django
from django.urls import path

# Views
from . import views

app_name = "carro"

urlpatterns = [
    path("agregar/<int:product_id>/", views.add_producto, name="add"),
    path("eliminar/<int:product_id>/", views.delete_product, name="delete"),
    path("restar/<int:product_id>/", views.subtract_product, name="substract"),
    path("limpiar/", views.empty_car, name="empty"),
]