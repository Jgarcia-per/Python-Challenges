from preparacion.guarderia import Guarderia
from preparacion.perro import Perro
from concentrado.concentrado import Concentrado

# llenamos concentrados
concentrado_1 = Concentrado("AcanaAcana 5", 165134, 3500, "INVIMA-AB-5123455")
concentrado_2 = Concentrado("Agility GoldAgility Gold 6", 200000, 4000, "INVIMA-AC-1764597")
concentrado_3 = Concentrado("CibauCibau 14", 170000, 5000, "INVIMA-AD-8234587")
concentrado_4 = Concentrado("Diamond CareDiamond Care 4", 100000, 800, "INVIMA-CA-1934597")
concentrado_5 = Concentrado("Diamond NaturalsDiamond Naturals 9", 300000, 1200, "INVIMA-BD-1638567")
concentrado_6 = Concentrado("Dog ChowDog Chow 5", 90000, 800, "INVIMA-PL-8234967")
concentrado_7 = Concentrado("Dr.Clauder'sDr.Clauder's 12", 320000, 6500, "INVIMA-AZ-2457657")
concentrado_8 = Concentrado("EvolveEvolve 8", 700000, 7000, "INVIMA-IT-1285678")

# llenamos guarderia
guarderia_1 = Guarderia('MADE HOME', 'Calle 15 sur #16 b', ['AcanaAcana 5','Dog ChowDog Chow 5',  'Agility GoldAgility Gold 6'])
guarderia_2 = Guarderia('Dogtor', 'Kra 7 norte #19 a', ['AcanaAcana 5', 'EvolveEvolve 8', 'CibauCibau 14', "Dr.Clauder'sDr.Clauder's 12"])

# llenamos perros
perro_1 = Perro("Zeus", "Bulldog", 54.5, 8,  "Dr.Clauder'sDr.Clauder's 12")
perro_2 = Perro("Princesa", "Pit Bull Terrier Americano", 40, 3, "Dog ChowDog Chow 5")
perro_3 = Perro("Manchas", "Dálmata", 20, 1, "EvolveEvolve 8")
perro_4 = Perro("Mateo", "Golden retriever", 32.5, 4, "AcanaAcana 5")
perro_5 = Perro("Rufus", "West Highland white terrier", 10.5, 3, "Agility GoldAgility Gold 6")

# concdicional basico
perro_guarderia = str(input('Ingrese el nombre del perro al que le quiera buscar una guarderia'))

# if (perro_guarderia == )