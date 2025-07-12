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

# Inversión lógica
# Pregunta si un número es divisible entre 3 o 5.
# Imprime False si lo es, True si no lo es (usa not para invertir el resultado).

# Contraseña segura
# Una contraseña es segura si:

# Tiene más de 8 caracteres

# Y contiene el carácter @

# O contiene el carácter #
# Verifica esto usando operadores lógicos.

# 🧪 Nivel Avanzado
# Sistema de acceso condicional
# Verifica si un usuario puede acceder a una zona restringida:

# Es administrador o tiene un pase de seguridad y su acceso no está suspendido.
# Usa variables como es_admin, tiene_pase, suspendido.

# Juego de lógica
# Tienes tres valores booleanos: a, b, c.
# Imprime True si exactamente dos de ellos son True.