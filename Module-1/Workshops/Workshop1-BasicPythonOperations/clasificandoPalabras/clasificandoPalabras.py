def llenar_lista():
    lista_vacia = []
    cantidad = int(input('Bienvenido\ncuantas palabras desea ingresar: '))
    for i in range(cantidad):
        palabraInput = input(f'Ingrese la palabra numero {i + 1}: ')
        lista_vacia.append(palabraInput)
    
    return lista_vacia
    
def describir_palabras():
    diccionario_palabras = {}
    lista_palabras = llenar_lista()
    
    for palabra in lista_palabras:
        diccionario_palabras[palabra] = len(palabra)
    
    return diccionario_palabras



print(describir_palabras())
