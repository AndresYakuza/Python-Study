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


# ======= Contador hacia atrás
# Pide un número y cuenta desde ese número hasta 0.

number = int(input('Digite numero: '))

while number >= 0:
    print(number, end=' ')
    number -= 1

print("\nDespegue.")

# 🟡 Normales
# Objetivo: Usar while con condiciones y lógica simple.

# ======== Adivina el número
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


#========= Menú de opciones
# Muestra un menú en pantalla con opciones:
# 1. Saludar
# 2. Decir adiós
# 3. Salir
# Repite el menú hasta que el usuario elija salir.

opcion = 0

while opcion != 3:
        print('# Menú de opciones')
        print('# 1. Saludar')
        print('# 2. Decir adiós')
        print('# 3. Salir')

        try:
            opcion = int(input('Opción: '))
            if opcion == 1: 
                print('=================')
                print('Hola! Saludos :)')
                print('=================')
            elif opcion == 2:
                print('=================')
                print('Bye! Regresa pronto :)')
                print('=================')
            elif opcion == 3:
                print('=================')
                print('Ohh! Saliste exitosamente :)')
                print('=================')
            else:
                print('=================')  
                print('Error, opción no valida...')
                print('=================')
        except ValueError:
            print('=======================================')  
            print('Error: debes ingresar un número válido.')
            print('=======================================')
# NOTA
# El bloque try-except se usa para manejar errores en tiempo de ejecución.
# El código dentro de try se ejecuta normalmente, y si ocurre un error,
# el bloque except captura la excepción y permite manejarla sin que el programa se detenga.

# ======== Multiplicación hasta acertar
# Pide dos números, calcula la multiplicación.
# Luego pide al usuario que diga el resultado.
# Repite hasta que acierte.

nu1 = int(input('Ingrese el primer número: '))
nu2 = int(input('Ingrese el segundo número: '))
result = nu1 * nu2

user_result = None  # Valor inicial que no puede ser igual al resultado

while user_result != result:
    user_result = int(input(f'¿Cuánto es {nu1} x {nu2}? '))
    
    if user_result == result:
        print(f'✅ ¡Correcto! {nu1} x {nu2} = {result}')
    else:
        print('❌ Incorrecto. Intenta de nuevo...\n')

# Nota
# None es un objeto especial en Python que representa la ausencia de valor o "nada".
# Se usa cuando quieres declarar una variable, pero aún no tiene un valor definido.

# 🔴 Difíciles (pero accesibles)
# Objetivo: Pensar un poco más, usar varias condiciones o más lógica.

# ========= Validar contraseña
# La contraseña correcta es "python123".
# Pide al usuario que escriba la contraseña.
# Solo tiene 3 intentos. Si se equivoca 3 veces, muestra "bloqueado".

passwordT = 'python123'
user_password = None
tries = 3

while user_password != passwordT:
    user_password = input('Digite la contraseña por favor: ')

    if user_password != passwordT:
        if tries > 1:
            tries -= 1
            print('=======================================')  
            print('❌ Incorrecto. Intenta de nuevo...')
            print(f'Te quedan {tries} intento/s, si llega a 0 procederemos a bloquear...')
            print('=======================================')  
        else: 
            print('=======================================')  
            print('❌BLOQUEADO❌ Has sobrepasado el numero de intentos...')
            print('=======================================')  
            break
    else:
        print('=======================================')  
        print('✅ ¡Correcto!')
        print('=======================================')  



# ======= Número mayor
# Pide números al usuario hasta que escriba -1.
# Al final muestra cuál fue el número mayor que escribió.

    
numbers_save = []
numbers = None

while numbers != -1:

    try: 
        numbers = int(input('Digite numeros (-1 para romper el siglo...): '))
        numbers_save.append(numbers)

    except ValueError:
        print('Error, no es un valor numerico...')

else:
    numbers_save.remove(-1)

    if numbers_save:
        print(f'Numeros digitados:{numbers_save}')
        print(f'Cantidad: {len(numbers_save)}')
        print(f'Numero mayor: {max(numbers_save)}')
        print(f'Numero menor: {min(numbers_save)}')
    else:
        print('No se ingresaron números válidos.')

# ======== Suma de pares
# Pide números hasta que el usuario escriba 0.
# Suma solo los números pares e imprime el total al final.

numbers = None
numberslist = []
par = []
impar = []
totalpar = 0

while numbers != 0:

    try:
        numbers =  int(input('(Finalizar digitando (0) Número: '))
        numberslist.append(numbers)

        if numbers % 2 == 0:
            par.append(numbers)
            totalpar += numbers
        else:
            impar.append(numbers)

    except ValueError:
        print('No es un valor numerico...')
    
else:

    par.remove(0)

    if numberslist: 

        if par: 
            print(f'Numeros pares: {par}')
            print(f'Suma total pares: {totalpar}')
        else:
            print('No se encotraron numeros pares')
        
        if impar:
            print(f'Número impares: {impar}')
        else:
            print('No se encotraron numeros impares')

    else:
        print('No se encotraron valores')