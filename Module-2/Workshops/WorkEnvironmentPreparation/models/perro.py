class Perro:
    def __init__(self, nombre: str, raza: str, peso: float, edad: int):
        self.__nombre = nombre
        self.__raza = raza
        self.__peso = peso
        self.__edad = edad

    def ladrar(self) -> str:
        return "¡Guau, guau!"

    def modificar_peso(self, nuevo_peso):
        self.peso = nuevo_peso

    def get_nombre_perro(self) -> str:
        return self.__nombre
    
    def get_raza_perro (self) -> str:
        return self.__raza
    
    def get_edad_perro (self) -> str:
        return self.__edad
    
    def retornar_perros (self):
        return {
            'nombre': self.__nombre, 
            'raza': self.__raza, 
            'peso': self.__peso, 
            'edad': self.__edad
            }