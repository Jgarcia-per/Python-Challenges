from ingrediente import Ingrediente

class Base(Ingrediente):
    def __init__(self, nombre, precio, calorias, inventario, es_vegetariano, sabor):
        super().__init__(nombre, precio, calorias, inventario, es_vegetariano)
        self._sabor = sabor

    def get_sabor(self):
        return self._sabor

    def set_sabor(self, sabor):
        self._sabor = sabor

    def reabastecer(self):
        self._inventario += 5
