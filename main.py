


# Verificar cuántos números son múltiplos de 3
# Pide al usuario que ingrese 10 números. Muestra cuántos son múltiplos de 3.

numeros = []
multiplos_de_3 = []

for i in range(1, 11):
    while True:
        try:
            entrada = input(f'Número {i}: ')
            numero = int(entrada)
            numeros.append(numero)

            if numero % 3 == 0:
                multiplos_de_3.append(numero)
            break
        except ValueError:
            print('Número no válido, intenta de nuevo...')

print(f'\nNúmeros totales: {numeros}')
print(f'Múltiplos de 3: {multiplos_de_3}')
print(f'Cantidad de múltiplos de 3: {len(multiplos_de_3)}')







    





    
