class Concentrado:
    def __init__(self, nombre: str, precio: str, numero_calorias: float, registro_invima: str):
        self.__nombre = nombre
        self.__precio =precio
        self.__numero_calorias = numero_calorias
        self.__registro_invima = registro_invima


    def dar_nombre_concentrado(self) -> str:
        return self.__nombre