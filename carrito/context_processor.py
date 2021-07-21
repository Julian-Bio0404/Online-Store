"""Context porcessor."""

# Carrito class
from .carrito import Carrito


def total_carro(request):
    user = Carrito(request)
    total=0
    for key, value in request.session["carro"].items():
        total = total + float(value["price"])
    return {"total_carro": total}
