"""Carrito class."""


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")

        if not carro:
            carro = self.session["carro"] = {}
        #else:
        self.carro = carro

    def add(self, product):
        if str(product.id) not in self.carro.keys():
            self.carro[product.id] = {
                "product_id": product.id,
                "name": product.name,
                "price": str(product.price),
                "quantity": 1,
                "picture": product.picture.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(product.id):
                    value["quantity"] += 1
                    break
        self.save_carro()

    def save_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def delete(self, product):
        product.id = str(product.id)
        if product.id in self.carro:
            del self.carro[product.id]
            self.save_carro()

    def subtract_product(self, product):
        for key, value in self.carro.items():
            if key == str(product.id):
                value["quantity"] -= 1
                if value["quantity"] == 0:
                    self.delete(product)
                break
        self.save_carro()

    def empty_car(self):
        self.session["carro"] = {}
        self.session.modified = True

    def save_carro(self):
        self.session["carro"] = {}
        self.session.modified = True
