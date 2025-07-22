

# 3.4.6   LAB   Los fundamentos de las listas

# Escenario
# Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4, y 5.

# Tu tarea es:

# escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1)
# escribir una línea de código que elimine el último elemento de la lista (Paso 2)
# escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
# ¿Listo para este desafío?


# Lista inicial
numeros = [1, 2, 3, 4, 5]
print(f'======= {numeros} =======')

# Paso 1: Reemplazar el valor central
valor_reemplace = int(input('Ingrese el valor que reemplace el número central de la lista con un número entero: '))
indice_central = len(numeros) // 2
numeros[indice_central] = valor_reemplace
print(f'Paso 1 ejecutado: {numeros}')

# Paso 2: Eliminar el último elemento
del numeros[-1]
print(f'Paso 2 ejecutado: {numeros}')

# Paso 3: Imprimir la longitud actual de la lista
print(f'Paso 3 ejecutado: {len(numeros)}')

