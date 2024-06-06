from preparacion.guarderia import Guarderia
from preparacion.perro import Perro
from concentrado.concentrado import Concentrado
import pickle

perros = []
guarderias = []
concentrados = []


def llenarClases( aLlenar:str):
    
    if (aLlenar == 'concentrado'): 
        cantidad_concentrados = int(input("¿Cuántos concentrados tienes? "))
        for i in range(cantidad_concentrados):
            nombre = input(f"Introduce el nombre del concentrado {i+1}: ")
            precio = float(input(f"Introduce el precio de {nombre}: "))
            calorias = float(input(f"Introduce el numero de calorias de {nombre}: "))
            invima = str(input(f"Introduce el registro del INVIMA de {nombre}: "))
            concentrado = Concentrado(nombre, precio, calorias, invima)
            concentrados.append(concentrado)

            with open('datos\datos.pickle', 'wb') as archivo:
                pickle.dump(concentrados, archivo)

    elif (aLlenar == 'guarderia'): 
        cantidad_guarderia = int(input("¿Cuántas guarderias tienes? "))
        for i in range(cantidad_guarderia):
            nombre = input(f"Introduce el nombre de la guarderia {i+1}: ")
            ubicacion = str(input(f"Introduce la ubicacion de {nombre}: "))
            concentrado = concentrados
            guarderia = Guarderia(nombre, ubicacion, concentrado)
            guarderias.append(guarderia)

    elif (aLlenar == 'perro'):
        cantidad_perros = int(input("¿Cuántos perros tienes? "))
        for i in range(cantidad_perros):
            nombre = input(f"Introduce el nombre del perro {i+1}: ")
            raza = str(input(f"Introduce la raza de {nombre}: "))
            peso = float(input(f"Introduce el peso de {nombre}: "))
            edad = int(input(f"Introduce la edad de {nombre}: "))
            nombre_concentrado = str(input(f"Introduce el nombre del concentrado para {nombre}: "))
            if nombre_concentrado in concentrados:
                perro = Perro(nombre, raza, peso, edad, nombre_concentrado)
                perros.append(perro)
            else:
                print ('Verifique el nombre del concentrado!')
    else:
        print(f'Verifique que desea llenar!\nel valor {aLlenar}, no existe')

print(llenarClases('concentrado'))


