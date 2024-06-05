import areaCirculo.circulo as funcionCirculo

def calcular_area_cuadrado(radio):
    area = (radio * 2) ** 2
    return round(area, 2)

def calcular_area_sombreada(radio):
    area_cuadrado = calcular_area_cuadrado(radio)
    area_circulo = funcionCirculo.calcular_area_circulo(radio)
    area_sombreada = area_cuadrado - area_circulo
    return area_sombreada
