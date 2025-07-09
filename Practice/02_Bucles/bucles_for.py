# 🟢 Ejercicios Fáciles

# ======= Contar del 1 al 10
# Muestra los números del 1 al 10 usando un bucle for.

for i in range(1, 11):
    print(i, end=' ')

# ======= Mostrar cada letra de una palabra
# Pide al usuario una palabra y muestra cada letra por separado, una por línea.

palabra = input('Digite una palabra: ')
for i in palabra:
    print(i)

# ====== Sumar los números del 1 al 100
# Usa un bucle para sumar del 1 al 100 y muestra el resultado.

total = 0

for i in range(1, 101):
    total += i
print("La suma total del 1 al 100 es:", total)

# 🧠 Regla clave:
# Todo lo que esté con sangría debajo del for, se ejecuta en cada vuelta del bucle.
# Todo lo que esté al mismo nivel que el for (sin sangría) se ejecuta una sola vez, después del bucle.

# ====== Mostrar los números pares del 1 al 20
# Solo imprime los números pares entre 1 y 20.

pares = []

for i in range (1, 21):
    if i % 2 == 0:
        pares.append(i)
print('Numeros pares: ', pares)

# 🟡 Ejercicios Normales

# ======= Pedir 5 números y mostrarlos
# Pide al usuario 5 números y guárdalos en una lista. Al final, muestra todos los números ingresados.

numbers = []
for i in range(1, 6):
    while True:
        try: 
            numbers_user = int(input(f'Numero {i}: '))
            numbers.append(numbers_user)
            break #Se coloca el break, para salir del bucle del while una vez ingresado un numero valido.
        except ValueError:
            print("Por favor, ingresa un número válido.")
print('Los numeros son: ', numbers)

# ====== Tabla de multiplicar
# Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10.

numero = int(input('Numero para multiplicar: '))

for i in range(1, 11):
    result = i * numero
    print(f'{numero} x {i} = {result}')

# ===== Sumar los positivos
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

# ========= Contar cuántos números son pares e impares
# Pide 10 números al usuario y al final muestra cuántos fueron pares y cuántos impares.


pares = []
impares = []

for i in range(1, 11):
    while True:
        entrada = input(f'Digite el número {i}: ')
        try:
            user_number = int(entrada)
            if user_number % 2 == 0:
                pares.append(user_number)
            else:
                impares.append(user_number)
            break
        except ValueError:
            print(f'Error, "{entrada}" no es un número válido...')

print(f'\nCantidad de números pares: {len(pares)} ==== Números pares: {pares}')
print(f'Cantidad de números impares: {len(impares)} ==== Números impares: {impares}')

# 🔴 Ejercicios Difíciles

# ==== Número mayor y menor
# Pide al usuario que ingrese 7 números y muestra cuál fue el mayor y el menor.

numerostotales = []

for i in range(1, 8):
    while True:
        entrada = input(f'Digite el número {i}: ')
        try:
            user_number = int(entrada)
            numerostotales.append(user_number)
            break
        except ValueError:
            print(f'Error, "{entrada}" no es un número válido...')

print(f'\nEl número mayor fue: {max(numerostotales)} ==== El números menor fue: {min(numerostotales)}')



# ====== Pirámide de asteriscos
# Pide al usuario un número de filas, y muestra una pirámide de asteriscos. Ejemplo con 4:
# *
# **
# ***
# ****


try:
    entrada = input('Ingresa un número de filas: ')

    numerofilas = int(entrada)
    numerofilas += 1

    for i in range(1, numerofilas):
        caracter = '*'
        print(i * caracter)
except ValueError:
    print(f'Error, "{entrada}", no es un número valido...')

#### Simple
# try:
#     numerofilas = int(input('Ingresa un número de filas: '))

#     for i in range(1, numerofilas + 1):
#         print('*' * i)

# except ValueError:
#     print('Error: el valor ingresado no es un número válido.')

# ======= Promedio de una lista de números
# Pide al usuario 5 números y calcula el promedio.

numeros = []

for i in range(1, 6): 

    while True:

        try: 
            data = input(f'Numero {i}: ')
            user_num = int(data)
            numeros.append(user_num)
            break
        except ValueError:
            print('Error, valor no valido...')


promedio = sum(numeros) / i #len(numeros)
print('Numeros totales: ', numeros)
print('Promedio: ', promedio)

# ====== Verificar cuántos números son múltiplos de 3
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