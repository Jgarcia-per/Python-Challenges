from .base import Base
from .complemento import Complemento

class Heladeria:
    def __init__(self):
        self.ingredientes = []
        self.productos = []
        self.contador_ventas = 0

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def agregar_producto(self, producto):
        if len(self.productos) < 4:
            self.productos.append(producto)
        else:
            print("No se pueden agregar más de 4 productos a la vez.")

    def producto_mas_rentable(self):
        if not self.productos:
            return None
        producto_rentable = max(self.productos, key=lambda p: p.calcular_rentabilidad())
        return producto_rentable

    def vender_producto(self, nombre_producto):
        producto = next((p for p in self.productos if p.get_nombre() == nombre_producto), None)
        if producto is None:
            print("El producto no está disponible en la heladería.")
            return False

        if self._verificar_ingredientes(producto):
            for ingrediente in producto.get_ingredientes():
                if isinstance(ingrediente, Base):
                    ingrediente.set_inventario(ingrediente.get_inventario() - 0.2)
                elif isinstance(ingrediente, Complemento):
                    ingrediente.set_inventario(ingrediente.get_inventario() - 1)
            self.contador_ventas += producto.get_precio_publico()
            print(f"Producto '{nombre_producto}' vendido.")
            return True
        else:
            print("No hay suficientes ingredientes para vender este producto.")
            return False

    def _verificar_ingredientes(self, producto):
        for ingrediente in producto.get_ingredientes():
            if ingrediente.get_inventario() < 1:
                return False
        return True

    def get_ingredientes(self):
        return self.ingredientes
    
    def get_productos(self):
        return self.productos
    
    def get_contador_ventas(self):
        return self.contador_ventas

    def set_ingredientes(self, ingredientes):
        self.ingredientes = ingredientes
    
    def set_productos(self, productos):
        self.productos = productos
    
    def set_contador_ventas(self, contador_ventas):
        self.contador_ventas = contador_ventas
