"""Context porcessor."""

# Carrito class
from .carrito import Carrito


def total_carro(request):
    user = Carrito(request)
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total(float(value["price"]) * value["quantity"])
        print("Hola")
    return {"total_carro": total}
