from .iproducto import Producto

class Copa(Producto):
    def __init__(self, nombre, precio_publico, ingredientes, tipo_vaso):
        self._nombre = nombre
        self._precio_publico = precio_publico
        self._ingredientes = ingredientes
        self._tipo_vaso = tipo_vaso

    def get_nombre(self):
        return self._nombre
    
    def get_precio_publico(self):
        return self._precio_publico
    
    def get_ingredientes(self):
        return self._ingredientes
    
    def get_tipo_vaso(self):
        return self._tipo_vaso

    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_precio_publico(self, precio_publico):
        self._precio_publico = precio_publico
    
    def set_ingredientes(self, ingredientes):
        self._ingredientes = ingredientes
    
    def set_tipo_vaso(self, tipo_vaso):
        self._tipo_vaso = tipo_vaso

    def calcular_costo(self):
        return sum(ingrediente.get_precio() for ingrediente in self._ingredientes)

    def calcular_rentabilidad(self):
        costo = self.calcular_costo()
        return self._precio_publico - costo

    def calcular_calorias(self):
        return sum(ingrediente.get_calorias() for ingrediente in self._ingredientes) * 0.95
