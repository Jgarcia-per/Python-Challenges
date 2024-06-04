import areaCuadrado.modulo as funcionSombra

def llamar_area_sombreada(radio):
    resultado = funcionSombra.calcular_area_sombreada(radio)
    return resultado


radio = float(input("Ingrese el radio: "))
area = funcionSombra.calcular_area_sombreada(radio)
print(f"La diferencia es: {area}")