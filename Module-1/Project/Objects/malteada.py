from .iproducto import Producto

class Malteada(Producto):
    def __init__(self, nombre, precio_publico, ingredientes, volumen):
        self._nombre = nombre
        self._precio_publico = precio_publico
        self._ingredientes = ingredientes
        self._volumen = volumen

    def get_nombre(self):
        return self._nombre
    
    def get_precio_publico(self):
        return self._precio_publico
    
    def get_ingredientes(self):
        return self._ingredientes
    
    def get_volumen(self):
        return self._volumen

    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_precio_publico(self, precio_publico):
        self._precio_publico = precio_publico
    
    def set_ingredientes(self, ingredientes):
        self._ingredientes = ingredientes
    
    def set_volumen(self, volumen):
        self._volumen = volumen

    def calcular_costo(self):
        return sum(ingrediente.get_precio() for ingrediente in self._ingredientes) + 500

    def calcular_rentabilidad(self):
        costo = self.calcular_costo()
        return self._precio_publico - costo

    def calcular_calorias(self):
        return sum(ingrediente.get_calorias() for ingrediente in self._ingredientes) + 200
