from abc import ABC, abstractmethod

class Ingrediente(ABC):
    def __init__(self, nombre: str, precio: float, calorias: float, inventario: str, es_vegetariano: bool):
        self._nombre = nombre
        self._precio = precio
        self._calorias = calorias
        self._inventario = inventario
        self._es_vegetariano = es_vegetariano
    
    # Getters
    def get_nombre(self):
        return self._nombre
    
    def get_precio(self):
        return self._precio
    
    def get_calorias(self):
        return self._calorias
    
    def get_inventario(self):
        return self._inventario
    
    def get_es_vegetariano(self):
        return self._es_vegetariano
    
    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_precio(self, precio):
        self._precio = precio
    
    def set_calorias(self, calorias):
        self._calorias = calorias
    
    def set_inventario(self, inventario):
        self._inventario = inventario
    
    def set_es_vegetariano(self, es_vegetariano):
        self._es_vegetariano = es_vegetariano
    
    def es_sano(self, numeroCalorias: int, vegetariano: bool) -> bool:
        if ((numeroCalorias < 100) or (vegetariano == True)):
            sano = True
        else:
            sano = False

        return sano

    @abstractmethod
    def reabastecer(self, cantidad):
        pass
    
