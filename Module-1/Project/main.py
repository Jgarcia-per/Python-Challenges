from Objects.base import Base
from Objects.complemento import Complemento
from Objects.copa import Copa
from Objects.heladeria import Heladeria
from Objects.ingrediente import Ingrediente
from Objects.iproducto import Producto 
from Objects.malteada import Malteada 

def main():
    ingrediente1 = Base(1500, 200, "Helado de Vainilla", 10, True, "Vainilla")
    ingrediente2 = Base(1600, 250, "Helado de Chocolate", 5, True, "Chocolate")
    ingrediente3 = Complemento(500, 100, "Sirope de Fresa", 20, True)
    ingrediente4 = Complemento(800, 150, "Crema Chantilly", 15, True)

    copa = Copa("Copa Vainilla", 5000, [ingrediente1, ingrediente3, ingrediente4], "Mediano")
    malteada = Malteada("Malteada Chocolate", 7000, [ingrediente2, ingrediente3, ingrediente4], 12)

    mi_heladeria = Heladeria()

    mi_heladeria.agregar_ingrediente(ingrediente1)
    mi_heladeria.agregar_ingrediente(ingrediente2)
    mi_heladeria.agregar_ingrediente(ingrediente3)
    mi_heladeria.agregar_ingrediente(ingrediente4)

    mi_heladeria.agregar_producto(copa)
    mi_heladeria.agregar_producto(malteada)

    mi_heladeria.vender_producto("Copa Vainilla")
    mi_heladeria.vender_producto("Malteada Chocolate")

    producto_rentable = mi_heladeria.producto_mas_rentable()
    if producto_rentable:
        print(f"El producto más rentable es: {producto_rentable.get_nombre()}")

if __name__ == "__main__":
    main()