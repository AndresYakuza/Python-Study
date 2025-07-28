"""
Archivo: retos_listas_matrices_comprehension.py
Descripción: Ejercicios de práctica sobre listas, comprensión de listas y matrices en Python.
"""

# 🟢 NIVEL 1: BÁSICO

# Crear una lista de los cuadrados de los números del 1 al 10
lista_cuadrado = [x**2 for x in range(1, 11)]
print("Cuadrados del 1 al 10:", lista_cuadrado)

# Filtrar los números impares del 1 al 20
numeros_impares = [x for x in range(1, 20) if x % 2 != 0]
print("Números impares del 1 al 20:", numeros_impares)

# Convertir todos los elementos de una lista de strings a mayúsculas
elementos = ['casa', 'python', 'osos']
convertidor = [x.upper() for x in elementos]
print("Elementos en mayúscula:", convertidor)

# Obtener una lista con los primeros 10 múltiplos de 3
multiplos_3 = [x for x in range(1, 31) if x % 3 == 0]
print("Primeros 10 múltiplos de 3:", multiplos_3)


# 🟡 NIVEL 2: INTERMEDIO

# De una lista de palabras, obtener las que tengan más de 4 letras
palabras = [x for x in elementos if len(x) > 4]
print("Palabras con más de 4 letras:", palabras)

# Reemplazar los números negativos de una lista con 0
numeros = [2, 3, 4, -4, -12, -1]
convertidor_negativos = [0 if x < 0 else x for x in numeros]
print("Negativos reemplazados con 0:", convertidor_negativos)

# Crear una lista de "par" o "impar" para los números del 1 al 10
etiquetas = [f'{x} - par' if x % 2 == 0 else f'{x} - impar' for x in range(1, 11)]
print("Par o impar del 1 al 10:", etiquetas)

# Obtener los caracteres únicos de una palabra (sin repetir)
palabra = 'ciencia'
caracteres_unicos = []
[caracteres_unicos.append(x) for x in palabra if x not in caracteres_unicos]
print("Caracteres únicos de 'ciencia':", caracteres_unicos)


# 🔴 NIVEL 3: AVANZADO

# Crear una matriz 5x5 con valores del 1 al 25
filas = 5
columnas = 5
matriz = [[x * columnas + j + 1 for j in range(columnas)] for x in range(filas)]
print("Matriz 5x5:")
for fila in matriz:
    print(fila)

# De una matriz dada, reemplazar los valores impares por "X" y los pares por el mismo valor
matriz_modificada = [[x * columnas + j + 1 if (x * columnas + j + 1) % 2 == 0 else "X" for j in range(columnas)] for x in range(filas)]
print("Matriz con impares como 'X':")
for fila in matriz_modificada:
    print(fila)

# Crear una tabla de multiplicar (del 1 al 10) usando listas anidadas
tabla_multiplicar = [[j * x for j in range(1, 11)] for x in range(1, 11)]
print("Tabla de multiplicar 1 al 10:")
for fila in tabla_multiplicar:
    print(fila)

# Dada una lista de strings, crear otra lista con la cantidad de vocales en cada string
lista_strings = ["hola", "mundo", "Python", "es", "genial"]
vocales = 'aeiou'
cantidad_vocales = [sum(palabra.lower().count(v) for v in vocales) for palabra in lista_strings]
print("Cantidad de vocales por palabra:", cantidad_vocales)


# 🧩 MINI RETO

# Generar una matriz 4x4 con números del 1 al 16:
# - Si el número es divisible por 3, reemplazarlo por "*"
# - Si no lo es, almacenar el cuadrado del número

filas = 4
columnas = 4
matriz_reto = [["*" if (x * columnas + j + 1) % 3 == 0 else (x * columnas + j + 1) ** 2 for j in range(columnas)] for x in range(filas)]
print("Matriz 4x4 del reto:")
for fila in matriz_reto:
    print(fila)
