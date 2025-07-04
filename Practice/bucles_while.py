
### While ####

# En general, en Python, un bucle se puede representar de la siguiente manera:

# while
#     instruction


######## Ejercicios practica ############

# 🟢 Fáciles

# =======  Contar del 1 al 10
# Muestra los números del 1 al 10 usando un bucle while.

number = 0
while number < 10:
    number += 1
    print('Numero:', number, end=' ')

# El parámetro end en print() define qué se imprime al final.
# Por defecto es un salto de línea (\n), pero se puede cambiar, por ejemplo a un espacio (" ").

# ======= Suma acumulada
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


# Contador hacia atrás

# nginx
# Copiar
# Editar
# Pide un número y cuenta desde ese número hasta 0.
# 🟡 Normales
# Objetivo: Usar while con condiciones y lógica simple.

# Adivina el número

# java
# Copiar
# Editar
# Guarda un número secreto (por ejemplo, 7).
# El usuario debe adivinarlo. El programa le dice si acertó o no.
# Usa while hasta que adivine.
# Menú de opciones

# markdown
# Copiar
# Editar
# Muestra un menú en pantalla con opciones:
# 1. Saludar
# 2. Decir adiós
# 3. Salir
# Repite el menú hasta que el usuario elija salir.
# Multiplicación hasta acertar

# nginx
# Copiar
# Editar
# Pide dos números, calcula la multiplicación.
# Luego pide al usuario que diga el resultado.
# Repite hasta que acierte.
# 🔴 Difíciles (pero accesibles)
# Objetivo: Pensar un poco más, usar varias condiciones o más lógica.

# Validar contraseña

# nginx
# Copiar
# Editar
# La contraseña correcta es "python123".
# Pide al usuario que escriba la contraseña.
# Solo tiene 3 intentos. Si se equivoca 3 veces, muestra "bloqueado".
# Número mayor

# cpp
# Copiar
# Editar
# Pide números al usuario hasta que escriba -1.
# Al final muestra cuál fue el número mayor que escribió.
# Suma de pares

# cpp
# Copiar
# Editar
# Pide números hasta que el usuario escriba 0.
# Suma solo los números pares e imprime el total al final.