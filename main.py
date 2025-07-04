# Suma acumulada


# Pide al usuario números uno por uno y súmalos.
# El programa termina cuando el usuario escribe 0.

numbers = int(input('Digite el numero: '))
total = 0
history = []

while numbers != 0:
    total += numbers
    history.append(numbers) # .append() agrega un valor al final de una lista
    print(f'Numeros digitados: {history}')
    print('Resultado: ', total)
    numbers = int(input('Digite el siguiente numero: '))

else:
    print('Finalizado.... Suma total: ', total)
    print('Cantidad de numeros ingresados: ', len(history)) # len(lista) devuelve la cantidad de elementos que hay en la lista
