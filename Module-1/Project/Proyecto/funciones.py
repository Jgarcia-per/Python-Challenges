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

def mejor_producto(producto1: dict, producto2: dict, producto3: dict, producto4: dict):
    productos = [producto1, producto2, producto3, producto4]
    mejorRentabilidad = productos[0]

    for producto in productos:
        if producto['rentabilidad'] > mejorRentabilidad['rentabilidad']:
            mejorRentabilidad = producto

    return mejorRentabilidad['nombre']

