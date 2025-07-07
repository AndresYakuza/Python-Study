

# Bucles en tu código con for

# Otro tipo de bucle disponible en Python proviene de la observación de que a veces es más importante contar los "giros o vueltas" del bucle que verificar las condiciones.

# for i in range(100):
#     # do_something()
#     pass

# la palabra reservada for abre el bucle for; nota - No hay condición después de eso; no tienes que pensar en las condiciones, ya que se verifican internamente, sin ninguna intervención.

# la función range() (esta es una función muy especial) es responsable de generar todos los valores deseados de la variable de control; en nuestro ejemplo, la función creará (incluso podemos decir que alimentará el bucle con) valores subsiguientes del siguiente conjunto: 0, 1, 2 .. 97, 98, 99; nota: en este caso, la función range() comienza su trabajo desde 0 y lo finaliza un paso (un número entero) antes del valor de su argumento.

# nota la palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto; es una instrucción vacía - la colocamos aquí porque la sintaxis del bucle for exige al menos una instrucción dentro del cuerpo (por cierto - if, elif, else y while expresan lo mismo).

# ==== IMPORTANTE ===== 

# La función range() puede recibir entre 1 y 3 argumentos:

# range(inicio, fin, paso)
# inicio: desde dónde empieza 
# fin: hasta dónde va 
# paso: de cuánto en cuánto avanza (por defecto es 1)

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

# Contar cuántos números son pares e impares
# Pide 10 números al usuario y al final muestra cuántos fueron pares y cuántos impares.

# 🔴 Ejercicios Difíciles
# Número mayor y menor
# Pide al usuario que ingrese 7 números y muestra cuál fue el mayor y el menor.

# Pirámide de asteriscos
# Pide al usuario un número de filas, y muestra una pirámide de asteriscos. Ejemplo con 4:

# markdown
# Copiar
# Editar
# *
# **
# ***
# ****
# Promedio de una lista de números
# Pide al usuario 5 números y calcula el promedio.

# Verificar cuántos números son múltiplos de 3
# Pide al usuario que ingrese 10 números. Muestra cuántos son múltiplos de 3.