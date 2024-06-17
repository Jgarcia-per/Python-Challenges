class cuidandero:
    def __init__(self, nombre: str, documento: int):
        self.__nombre = nombre
        self.__documento = documento

    def get_nombre_cuidandero(self) -> str:
        return self.__nombre