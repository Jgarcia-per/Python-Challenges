def estoSano (numeroCalorias: int, vegetariano: bool) -> bool:
    if ((numeroCalorias < 100) or (vegetariano == True)):
        sano = True
    else:
        sano = False

    return sano

def calorias(calorias: list[int]) -> float:
    sumaCalorias = 0

    for i in calorias:
        sumaCalorias += i
    resultado = round(sumaCalorias * 0.95, 2)

    return resultado

def costos(ingrediente1: dict, ingrediente2: dict, ingrediente3: dict) -> float:
    precio1 = ingrediente1["precio"]
    precio2 = ingrediente2["precio"]
    precio3 = ingrediente3["precio"]

    costo_total = precio1 + precio2 + precio3

    return costo_total

def rentabilidad(producto1: dict, producto2: dict, producto3: dict, precio_total: int) -> float:
    resultadoCostos = costos(producto1, producto2, producto3)

    rentabilidad = precio_total / resultadoCostos 

    return rentabilidad


producto1 = {"nombre": "Helado de Fresa", "precio": 1200}
producto2 ={"nombre": "Chispas de chocolate", "precio": 500}
producto3 = {"nombre": "Mani Japonés", "precio": 900}

costo = rentabilidad(producto1, producto2, producto3, 7500)
print(f"la restabilidad fue de ${costo}")

