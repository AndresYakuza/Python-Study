
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
