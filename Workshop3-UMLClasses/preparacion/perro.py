from concentrado.concentrado import Concentrado

class Perro:
    def __init__(self, nombre: str, raza: str, peso: float, edad: int, concentrado: Concentrado):
        self.__nombre = nombre
        self.__raza = raza
        self.__peso = peso
        self.__edad = edad
        self.__concentrado = concentrado

    def ladrar(self) -> str:
        return "¡Guau, guau!"

    def modificar_peso(self, nuevo_peso):
        self.peso = nuevo_peso

    def dar_nombre_perro(self) -> str:
        return self.__nombre