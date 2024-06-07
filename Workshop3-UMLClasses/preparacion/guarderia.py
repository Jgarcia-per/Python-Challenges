class Guarderia: 
    def __init__(self, nombre: str, ubicacion: str, concentrado: list):
        self.__nombre = nombre
        self.__ubiacion = ubicacion
        self.__concentrado = concentrado

    def get_nombre_guarderia (self) -> str :
        return self.__nombre