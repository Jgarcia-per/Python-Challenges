from .ingrediente import Ingrediente

class Complemento(Ingrediente):
    def __init__(self, nombre, precio, calorias, inventario, es_vegetariano):
        super().__init__(nombre, precio, calorias, inventario, es_vegetariano)

    # Implementación del método abstracto reabastecer
    def reabastecer(self):
        self._inventario += 10

    # Método específico para renovar el inventario a 0
    def renovar_inventario(self):
        self._inventario = 0