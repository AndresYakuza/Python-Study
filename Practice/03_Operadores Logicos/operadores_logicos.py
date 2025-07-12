# 🧠 Nivel Básico
# Par o mayor de edad
# Escribe un programa que pregunte al usuario su edad y un número.
# Imprime True si es mayor de edad o si el número es par.

edad = int(input('Edad: '))
numero = int(input('numero: '))

if edad >= 18 or numero % 2 == 0:
    print(True)
else:
    print(False)

# Nombre y contraseña correctos
# Verifica si el nombre de usuario es "admin" y la contraseña es "1234".
# Imprime Acceso concedido si ambas condiciones son verdaderas.

user = 'admin'
password = '1234'

us = input('Usuario: ')
pa = input('Password: ')

if user == us and password == pa: 
    print('Acceso concedido')
else:
    print('Acceso denegado')


# Número dentro de rango
# Verifica si un número ingresado por el usuario está entre 10 y 50.
# Usa operadores lógicos para resolverlo.

numero = int(input('Numero: '))

if numero >=  10 and numero <= 50:
    print('Positivo')
else:
    print('Negativo')

# ⚙️ Nivel Intermedio
# Validar entrada múltiple
# Pregunta al usuario su edad y si tiene licencia (s o n).
# Imprime si puede manejar: edad ≥ 18 y licencia == "s"

edad = int(input('¿Cuál es tu edad? '))

while True:
    licencia = input('¿Tienes licencia para conducir? (s o n): ').lower()
    if licencia not in ['s', 'n']:
        print('Entrada no válida. Por favor, responde con "s" o "n".')
        continue
    elif edad >= 18 and licencia == 's':
        print('✅ Puedes manejar.')
    else:
        print('❌ No puedes manejar.')
    break

# Inversión lógica
# Pregunta si un número es divisible entre 3 o 5.
# Imprime False si lo es, True si no lo es (usa not para invertir el resultado).

numero = int(input('Digite el número del cual desea saber si es divisible entre 3 o 5: '))

if numero % 3 == 0 or numero % 5 == 0:
    print(not(True))
else:
    print(not(False))

# Simple 
# numero = int(input('Digite el número del cual desea saber si es divisible entre 3 o 5: '))
# print(not (numero % 3 == 0 or numero % 5 == 0))


# Contraseña segura
# Una contraseña es segura si:

# Tiene más de 8 caracteres
# Y contiene el carácter @
# O contiene el carácter #

# Verifica esto usando operadores lógicos.

contrasena = input('Digite la contraseña: ')

if len(contrasena) > 8 and ('#' in contrasena or '@' in contrasena):
    print('Su contraseña es seguro')
else:
    print('Su contraseña no cumple con los requisitos.')


# 🔢 Número fuera de rango (negación)
# Crea un programa que pregunte al usuario por un número.
# Imprime "Fuera de rango" si no está entre 100 y 200, ambos inclusive.
# Usa el operador not o una negación lógica.

# 🧪 Nivel Avanzado
# Sistema de acceso condicional
# Verifica si un usuario puede acceder a una zona restringida:

# Es administrador o tiene un pase de seguridad y su acceso no está suspendido.
# Usa variables como es_admin, tiene_pase, suspendido.

# Juego de lógica
# Tienes tres valores booleanos: a, b, c.
# Imprime True si exactamente dos de ellos son True.

# 🎮 Sistema de puntos para premio
# Un usuario puede reclamar un premio si cumple con al menos dos de las siguientes condiciones:

# Tiene más de 1000 puntos

# Es cliente VIP

# Hace más de 1 año que está registrado

# Usa variables como: puntos, es_vip, años_registrado y operadores lógicos para verificar si cumple 2 o más condiciones.