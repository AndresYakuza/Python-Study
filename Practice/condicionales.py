
# IF - ELIF - ELSE 

# Obtener el numero mayor mediante un algoritmo 
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))
nummax = num1
if num2	> nummax:
    nummax = num2
if num3 > nummax:
    nummax = num3
print('El numero mayor es:', nummax)

#########################################################

# Espatifilo, más comúnmente conocida como la planta de Cuna de Moisés o flor de la paz, es una de las plantas para interiores más populares que filtra las toxinas dañinas del aire. Algunas de las toxinas que neutraliza incluyen benceno, formaldehído y amoníaco.

# Imagina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada en forma de la palabra Espatifilo, grite involuntariamente a la consola la siguiente cadena: "¡Espatifilo es la mejor planta de todas!"
# Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:
# imprima el enunciado "Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!" en la pantalla si la cadena ingresada es "ESPATIFILIO" (mayúsculas)
# imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo" (minúsculas)
# imprima "¡Espatifilo!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.
# Prueba tu código con los datos que te proporcionamos. ¡Y hazte de un Espatifilo también!

entrada = input('')
if entrada == 'ESPATIFILIO':
    print('Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!')
elif entrada == 'espatifilo':
    print('No, ¡quiero un gran Espatifilo!')
else:
    print(f'¡Espatifilo!, ¡No {entrada}!')


##############################################################

# Érase una vez una tierra de leche y miel - habitada por gente feliz y próspera. La gente pagaba impuestos, por supuesto - su felicidad tenía límites. El impuesto más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

# si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
# si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
# Tu tarea es escribir una calculadora de impuestos.

# Debe aceptar un valor de punto flotante: el ingreso.
# A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti - la encontrarás en el código de esqueleto del editor.
# Nota: este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). Ten esto en cuenta durante tus cálculos.

income = float(input("Introduce el ingreso anual: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

if tax < 0.0:
    tax = 0.0  # No puede ser negativo

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")


###################################################

# Como seguramente sabrás, debido a algunas razones astronómicas, el año puede ser bisiesto o común. Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.

# Desde la introducción del calendario Gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

# si el número del año no es divisible entre cuatro, es un año común.
# de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
# de lo contrario, si el número del año no es divisible entre 400, es un año común.
# de lo contrario, es un año bisiesto.
# Observa el código en el editor - solo lee un número de año y debe completarse con las instrucciones que implementan la prueba que acabamos de describir.

# El código debe mostrar uno de los dos mensajes posibles, que son Año Bisiesto o Año Común, según el valor ingresado.
# Sería bueno verificar si el año ingresado cae en la era Gregoriana y emitir una advertencia de lo contrario: No dentro del período del calendario Gregoriano. Consejo: utiliza los operadores != y %.

year = int(input("Introduce un año: "))

if year > 1582:
        if year % 4 != 0:
            print('Es un año común.')
        elif year % 100 != 0:
            print('Es un año bisiesto.')
        elif year % 400 != 0:
            print('Es un año común.')
        else:
            print('Es un año bisiesto.')
else:
    print("No esta dentro del período del calendario Gregoriano")



#######################################################

# 🔸 Ejercicio 1: Edad para votar
# Pide al usuario su edad e imprime:
# "Puedes votar" si tiene 18 años o más.
# "No puedes votar" si es menor de 18.

edad = int(input('Por favor digite su edad: '))

if edad >= 18:
    print('Puedes votar.')
else:
    print('No puede votar.')

# 🔸 Ejercicio 2: Número par o impar
# Pide un número entero y muestra si es "Par" o "Impar".

numero = int(input('Por favor digite el numero: '))

if numero % 2 == 0:
    print('El número es par.')
else:
    print('El número es impar.')


# 🔸 Ejercicio 3: Clasificación de nota
# Pide una nota del 0 al 10. Según la nota, muestra:

# "Sobresaliente" si es 9 o 10.

# "Notable" si es 7 u 8.

# "Aprobado" si es 5 o 6.

# "Suspenso" si es menor de 5.


nota = int(input('Digite por favor la nota en el rango de 0 a 10: '))

if nota >= 0 or nota <= 10: # Correcion if 0 <= nota <= 10:
    if nota < 5:
        print('Suspenso')
    elif nota == 5 or nota == 6:
        print('Aprobado')
    elif nota == 7 or nota == 8:
        print('Notable')
    else:
        print('Sobresaliente')
else:
    print('Nota no valida.')


# 🔸 Ejercicio 4: Calculadora simple
# Pide dos números y una operación (+, -, *, /). Muestra el resultado.

n1 = int(input('Digite el primer valor: '))
n2 = int(input('Digite el segundo valor: '))
ope = int(input('Digite el numero de la operacion a realizar... (1)Suma (2)Resta (3)Multiplicacion (4)División'))

if ope == 1:
    print('Usted ha seleccionado suma.')
    print('El resultado de su suma es:', n1 + n2)
elif ope == 2:
    print('Usted ha seleccionado resta.')
    print('El resultado de la resta es:', n1 - n2)
elif ope == 3:
    print('Usted ha seleccionado multiplicacion.')
    print('El resultado de su multiplicacion es:', n1 * n2)
elif ope == 4:
    print('Usted ha seleccionado división')
    print('El resultado de su division es:', n1 / n2)
else:
    print('Opción no valida.')

# 🔸 Ejercicio 5: Año bisiesto (repetición del que hiciste, sin aviso del calendario Gregoriano)

year = int(input("Introduce un año: "))

if year % 4 != 0:
    print('Es un año común.')
elif year % 100 != 0:
    print('Es un año bisiesto.')
elif year % 400 != 0:
    print('Es un año común.')
else:
    print('Es un año bisiesto.')

# 🔸 Ejercicio 6: Contraseña segura
# Define una contraseña en tu código (por ejemplo: "python2025").
# Pide al usuario que introduzca la contraseña.
# Si es correcta, imprime "Acceso concedido", si no, "Contraseña incorrecta".

contrasena = input('Por favor digite la contrasena: ')

if contrasena == 'python2025': # Detalle -- if contrasena.lower() == 'python2025':
    print('Acceso concedido')
else:
    print('Acceso denegado.')

# 🔸 Ejercicio 7: Mayor de tres números
# Pide tres números al usuario e imprime cuál es el mayor.

nu1 = int(input('Digite el primer numero: '))
nu2 = int(input('Digite el segundo numero: '))
nu3 = int(input('Digite el tercer numero: '))

numayor = 1 # Detalle -- n1

if numayor > nu2:
    numayor = nu2

if numayor > nu3:
    numayor = nu3

print('El numero mayor es:', numayor)


#########################################################

# 🔸 Ejercicio 1: Calculadora avanzada
# Pide dos números y la operación que desea realizar:

# Suma
# Resta
# Multiplicación
# División
# Potencia
# Módulo (resto de la división)

# El usuario puede elegir escribiendo el nombre de la operación (por ejemplo: "suma"). 
# Muestra el resultado. Si la operación no es válida, muestra un mensaje de error.


nume1 = int(input('Numero 1: '))
nume2 = int(input('Numero 2: '))
print('Por favor digitar el nombre de la operacion tal como se muestra en el enunciado.')
opera = input('Operacion a realizar: Suma, Resta, Multiplicación, División, Potencia, Módulo: ')

if opera.lower() == 'suma':
    print('Usted ha seleccionado suma.')
    print('El resultado de su suma es:', nume1 + nume2)
elif opera.lower() == 'resta':
    print('Usted ha seleccionado resta.')
    print('El resultado de la resta es:', nume1 - nume2)
elif opera.lower() == 'multiplicación':
    print('Usted ha seleccionado multiplicación.')
    print('El resultado de su multiplicación es:', nume1 * nume2)
elif opera.lower() == 'división':
    print('Usted ha seleccionado división')
    print('El resultado de su división es:', nume1 / nume2)
elif opera.lower() == 'potencia':
    print('Usted ha seleccionado potencia')
    print('El resultado de su potencia es:', nume1 ** nume2)
elif opera.lower() == 'módulo':
    print('Usted ha seleccionado módulo')
    print('El resultado de su módulo es:', nume1 % nume2)
else:
    print(f'Opción no valida. Por favor validar si {opera} es igual a las opciones solicitadas.')


#  🔸 Ejercicio 3: Pide un número al usuario e indica si:
# Es positivo
# Es negativo
# Es cero


valor1 = float(input('Valor numerico: '))

if valor1 < 0:
    print('Negativo')
elif valor1 == 0:
    print('Es cero')
else:
    print('Positivo')

#########################################################


# 🔸 Ejercicio 3: Conversor de temperatura
# El usuario escribe una temperatura y la unidad original (Celsius o Fahrenheit), 
# y el programa muestra la temperatura convertida a la otra unidad.

# Ejemplo:
# Si el usuario escribe 32 F, el programa devuelve 0 C.
# Si escribe 100 C, devuelve 212 F.



#########################################################

# 🔸 Ejercicio 4: Calculadora de sueldo con impuestos
# El usuario ingresa su sueldo bruto (antes de impuestos). Según el sueldo:

# Si es menor de 1000, paga 5% de impuestos.

# Entre 1000 y 2000, paga 10%.

# Más de 2000, paga 15%.

# El programa debe calcular y mostrar el sueldo neto (después de impuestos).


#########################################################

# 🔸 Ejercicio 5: Año bisiesto y día de la semana
# Pide al usuario que introduzca un año y un número de día (1 a 365 o 366).
# Calcula:

# Si es año bisiesto o no.

# Qué día de la semana corresponde (asumiendo que el 1 de enero de ese año es lunes).

# Ejemplo:
# Si el usuario pone 2024, día 3, diría: "Miércoles".

# (Pista: usar % para rotar entre los días de la semana).













