
def IMC():
    weight = int(input('Bienvenido\ningrese su peso: '))
    height = int(input('ingrese su altura: '))
    
    imc = round(weight/(height ** 2), 2)
    
    return imc



print(IMC())