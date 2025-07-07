# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# 🔴 Ejercicios con break
# 1. 🔐 Contraseña secreta
# Pide al usuario que ingrese una contraseña repetidamente.
# Si escribe "python123", muestra "Acceso concedido" y termina el bucle.
# Si no, muestra "Contraseña incorrecta" y vuelve a preguntar.

correct_password = 'python123'
while True:
    user_password = input('Digite la contraseña: ')
    if user_password == correct_password:
        print('Acceso concedido')
        break
    else:
        print('==========================================')
        print('Contraseña incorrecta, intenta de nuevo...')
        print('==========================================')

# 2. 🎯 Encuentra el número secreto
# Escribe un programa que genere un número aleatorio entre 1 y 10 (puedes usar random.randint).
# El usuario tiene intentos infinitos para adivinarlo.
# Cuando acierte, muestra "¡Correcto!" y termina el programa con break.

import random

randomnumber = random.randint(1, 10)

while True: 
    user_number = int(input('Numero a adivinar entre 1 y 10: '))

    if user_number == randomnumber:
        print("¡Correcto!")
        break
    else: 
        print('Incorrecto, de nuevo: ')

# 🟡 Ejercicios con continue
# 3. 🚫 Saltar los múltiplos de 3
# Imprime los números del 1 al 10, pero omite (no imprimas) los que sean múltiplos de 3.

for i in range(1, 11):
    if i % 3 == 0:
        continue  # ← aquí se salta el print si el número es múltiplo de 3
    print(i)  # solo se ejecuta si no se hizo continue

# 4. 🧹 Filtrar palabras prohibidas
# Pide al usuario que ingrese 5 palabras.
# Si alguna palabra es "cancelar", omite esa palabra y continúa con la siguiente sin agregarla a la lista.
# Al final, muestra la lista de palabras válidas.

grupo_palabras = []

for i in range(1, 6):
    palabras = input(f'Digite la palabra número {i}: ')

    if palabras == 'cancelar':
        continue
    
    grupo_palabras.append(palabras)
print(grupo_palabras)