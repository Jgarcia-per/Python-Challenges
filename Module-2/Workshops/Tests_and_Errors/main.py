from Class.ianimal import iAnimal
from Class.animal import Animal
from Class.animal_granja import Animal_Granja
from Class.perro import Perro
from Class.gato import Gato
from Class.animal_exotico import Animal_Exotico
from Class.huron import Huron
from Class.boa_constrictor import BoaConstrictor

perro_1 = Perro("Zeus", "Rottweiler", 45.8, 3)

print(f'\n\nEs perro: {isinstance(perro_1, Perro)}')
print(f'Es Animal: {isinstance(perro_1, Animal)}')
print(f'Es iAnimal: {isinstance(perro_1, iAnimal)}')
print(f'Es Animal_granja: {isinstance(perro_1, Animal_Granja)}\n\n')

# Animal Exotico
animal_exotico_1 = Animal_Exotico("Python", 25.0, 2, "India", 100.0)
print(f'Es animal exótico: {isinstance(animal_exotico_1, Animal_Exotico)}')
print(f'Flete del animal exótico: {animal_exotico_1.calcular_flete()}\n\n')

# Huron
huron_1 = Huron("Fuzz", 1.2, 2, "USA", 50.0)
print(f'Es Huron: {isinstance(huron_1, Huron)}')
print(f'Sonido del hurón: {huron_1.hacer_sonido()}\n\n')


# BoaConstrictor
boa_1 = BoaConstrictor("Nagini", 30.0, 5, "Brasil", 150.0)
boa_1.alimentar()
boa_1.alimentar()
print(f'Es BoaConstrictor: {isinstance(boa_1, BoaConstrictor)}')
print(f'Ratones comidos por la boa: {boa_1.get_ratones_comidos()}')
print(f'Sonido de la boa: {boa_1.hacer_sonido()}\n\n')

