from models.perro import Perro
from models.guarderia import Guarderia

perro_1 = Perro("Rufo", "Labrador", 22, 7)
perro_2 = Perro("Bingo", "Pug", 6, 2)
perro_3 = Perro("Lassie", "collie", 27, 5)

guarderia = Guarderia("Patitas Felices", "Kra 7 calle 45", ['DohChow', 'miringo', 'huellitas'])
guarderia.agregar_perro(perro_1)
guarderia.agregar_perro(perro_2)
guarderia.agregar_perro(perro_3)

class Controller:
    def retornar_perros():
        return guarderia.obtener_perros()