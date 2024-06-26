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

    def get_nombre_perro(self) -> str:
        return self.__nombre
    
    def get_concentrado_favorito(self) -> str:
        return self.__concentrado
    
    def get_raza_perro (self) -> str:
        return self.__raza