
# Adivina el número
# Guarda un número secreto (por ejemplo, 7).
# El usuario debe adivinarlo. El programa le dice si acertó o no.
# Usa while hasta que adivine.
import random

secret_number = random.randint(1, 10)
user_number = int(input('Adivina un numero del 1 al 10: '))
intentos = []

while secret_number != user_number:
    intentos.append(user_number)
    print('======================================')
    print('Ups! Numero equivocado, try again...')
    print('Numeros ingresados: ', intentos)
    user_number = int(input('Adivina un numero nuevamente del 1 al 10: '))


else:
    print('======================================')
    print('NAISUT! Excelente, adivinaste!')
    print('Total de intentos: ', len(intentos))


