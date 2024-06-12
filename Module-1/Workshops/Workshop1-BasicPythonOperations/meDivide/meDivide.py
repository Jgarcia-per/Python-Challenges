def numeros_divisibles(n1, n2):
    divisibles = []
    
    for num in range(1, 101):
        if num % n1 == 0 and num % n2 == 0:
            divisibles.append(num)
    
    return divisibles

n1 = int(input('Bienvenido\ningrese un numero: '))
n2 = int(input('ingrese otro numero: '))
resultado = numeros_divisibles(n1, n2)
print(resultado)
