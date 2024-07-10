from .boa_constrictor import BoaConstrictor
from .huron import Huron

class Guarderia:
    def __init__(self):
        self.boas = [BoaConstrictor('Boa1', 15.0, 5, 'Brasil', 5.0), 
                     BoaConstrictor('Boa2', 20.0, 7, 'Colombia', 7.0)]
        self.hurones = [Huron('Huron1', 2.0, 3, 'Argentina', 3.0), 
                        Huron('Huron2', 2.5, 4, 'Chile', 4.0)]

    def alimentar_boa(self, boa: BoaConstrictor) -> str:
        if boa is None:
            return "Esta Boa no existe!"
        try:
            result = boa.alimentar()
            if result == 'Demasiados Ratones!':
                return "La boa está llena"
            return "Éxito"
        except Exception as e:
            return str(e)