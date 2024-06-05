def leapYears():
    year = int(input('Bienvenido\n Ingrese un año: '))
    bisiesto = False
    
    if ((year % 4) == 0):
        if (((year % 100) and (year % 400)) == 0):
            bisiesto = True
            return bool(bisiesto)
        
    return bool(bisiesto)

print(leapYears())