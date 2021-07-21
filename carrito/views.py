"""Carrito views."""

# Django
from django.shortcuts import redirect

# Carrito
from .carrito import Carrito

# Models
from store.models import Product


def add_producto(request, product_id):
    carro = Carrito(request)
    product = Product.objects.get(id=product_id)
    carro.add(product=product)
    return redirect("Store")

def delete_product(request, product_id):
    carro = Carrito(request)
    product = Product.objects.get(id=product_id)
    carro.delete(product=product)
    return redirect("Store")

def subtract_product(request, product_id):
    carro = Carrito(request)
    product = Product.objects.get(id=product_id)
    carro.subtract_product(product=product)
    return redirect("Store")

def empty_car(request, product_id):
    carro = Carrito(request)
    carro.empty_car()
    return redirect("Store")

   