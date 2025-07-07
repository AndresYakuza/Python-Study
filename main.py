

# Sumar los positivos
# Pide 6 números y suma solo los que sean mayores que cero.

positivos = []
numeros = []
negativos = []
total = 0

for i in range(1, 7):
    while True:
        try:
            user = int(input(f'Numero {i}: '))
            numeros.append(user)

            if user > 0:
                total += user
                positivos.append(user)
            else:
                negativos.append(user)
            
            break  # Salimos del while cuando el input es válido

        except ValueError:
            print('Valor no válido. Intenta de nuevo.')

print('Numeros totales: ', numeros)
print('Numeros positivos: ', positivos)
print('Numeros negativos: ', negativos)
print('Suma de los positivos: ', total)





    





    
