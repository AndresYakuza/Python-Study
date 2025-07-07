# Ejercicios Faciles

# 1. Suma de dos números
# Crea dos variables con números enteros y muestra la suma en pantalla.

num1 = 10
num2 = 20
print('El resultado de la suma es:', num1+num2)

# 2. Área de un rectángulo
# Usa dos variables (base y altura) y calcula el área (base * altura).

base = 10
altura = 20 
area = base * altura
print('El area es:', area)

# 3. Intercambio de valores
# Crea dos variables con diferentes valores y luego intercambia sus contenidos.

V1 = "Esto es un texto"
V2 = 23
Variable1 = V2
Variable2 = V1
print("V1:", Variable1, "V2:", Variable2)

#### ERROR #### 

V1 = "Esto es un texto"
V2 = 23
V1, V2 = V2, V1  # Intercambio real
print("V1:", V1, "V2:", V2)



# 4. Mensaje personalizado
# Pide al usuario su nombre y edad, y luego imprime: "Hola [nombre], tienes [edad] años."

nombre = input('Digite por favor su nombre:')
edad = input('Digite por favor su edad:')
print(f'Hola, {nombre}. Tienes {edad} años!')


# 5. Conversión de temperaturas
# Declara una variable con una temperatura en grados Celsius y conviértela a Fahrenheit. Fórmula: F = C * 1.8 + 32

TemperaturaC = 100
print(TemperaturaC * 1.8 + 32)

#### Sugerencia ####

TemperaturaC = 100
fahrenheit = TemperaturaC * 1.8 + 32
print(f'{TemperaturaC}°C equivale a {fahrenheit}°F')



# Ejercicios Normales

# 1. Operaciones matemáticas
# Declara dos números y muestra su suma, resta, multiplicación y división.

Num1 = 22
Num2 = 23
suma = (Num1 + Num2)
resta = (Num1 - Num2)
multiplicacion = (Num1 * Num2)
division = (Num1 / Num2)
print(f'La suma es: {suma}, La resta es: {resta}, La multiplicación es: {multiplicacion} y la división es: {division}.')


# 2.	Edad en el futuro
# Pide al usuario su edad y calcula cuántos años tendrá en 10 años.

edad = input('Por favor digite su edad:')
edad = int(edad)
calculo = edad + 10
print('La edad en 10 años será:', calculo)


# 3.	Promedio de tres notas
# Declara tres variables con notas y calcula su promedio.

nota1 = 5.0
nota2 = 4.4
nota3 = 4.0
promedio = (nota1 + nota2 + nota3) / 3
print('Su promedio general fue de:', promedio)


# 4.	Dinero en la billetera
# Crea variables con diferentes cantidades de dinero (billetes y monedas) y suma el total.

monto1 = 10.44
monto2 = 4.44
monto3 = 32.44
total = (monto1 + monto2 + monto3)
print(f'Usted tiene un total de: ${total} dolares.')


# 5.	Tiempo en segundos
# Dado un tiempo en horas, minutos y segundos, calcula el total en segundos.

hora = input('Digite las horas:')
minuto = input('Digite los minutos:')
segundos = input('Digite los segundos:')

hora = int(hora)
minuto = int(minuto)
segundos = int (segundos)

HS = hora * 3600
MS = minuto * 60

conversion = HS + MS + segundos

print(f'La hora digitada: {hora}:{minuto}:{segundos} en segundos es {conversion} segundos.')


# Ejercicios Dificles 

# 1.	Interés compuesto
# o	Calcula el monto final con interés compuesto usando:
# A = P * (1 + r/n)^(nt)
# Donde:
# 	P es el capital inicial
# 	r es la tasa de interés anual
# 	n es el número de veces que se capitaliza al año
# 	t es el número de años

import math 

p = int(input('Digite el capital inicial: '))
r = int(input('Digite la tasa de interes anual:'))
n = int(input('Digite el numero de veces que se capitaliza al año:'))
t = int(input('Digite el numero de años:'))


a = round(p * (1 + r/n) + math.exp((n*t)))

print(f'El monto final con interes compuesto es de: {a}')


# 2.	Conversión de tiempo
# o	A partir de un total de segundos, calcula cuántas horas, minutos y segundos hay.

S = 10022

Hora = S // 3600
Minutos = (S % 3600) // 60
segundos = S % 60

print(f'EL tiempo es: {Hora} Horas, {Minutos} Minutos y {segundos} Segundos.')


# 3.	Salario con bonificaciones
# o	Pide el salario base y aplica una bonificación del 10% si el salario es menor de $1000, y del 5% si es mayor o igual.

salario = int(input('Por favor digite su salario en dolares: '))

if salario < 1000:
    bonificacion = (salario / 10) + salario
    print('Felicidades este es su salario mas bonificacion:', bonificacion)
elif salario >= 1000:
    bonificacion1 = (salario / 5) + salario
    print('Felicidades este es su salario mas bonificacion:', bonificacion1)


# 4.	Conversión de moneda
# o	Dado un monto en dólares y una tasa de cambio, conviértelo a euros.

dolares = 3333
tasa = 0.89
conversion = dolares * tasa 
print(conversion)


# 5.	División de cuenta
# o	Dado el total de una cuenta y la cantidad de personas, divide el total. Si hay propina, añádela antes de dividir.

persona = int(input('Cuantas personas hay en total: '))
cuenta = int(input('Cuanto es la cuenta total: '))
propina = input('¿Hay propina? (si/no): ').strip().lower()

if propina == 'si':
    cantidad = int(input('¿De cuanto es la propina? = '))
    total = (cuenta + cantidad) / persona
    print(f'A cada persona le corresponde pagar: ${total:.2f}')

else:
    total1 = cuenta / persona
    print(f'A cada persona le corresponde pagar: ${total1:.2f}')











