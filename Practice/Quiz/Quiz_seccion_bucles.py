# Pregunta 1: Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:

for i in range(0, 11):
    if i % 2 != 0:
        print(i)

# Pregunta 2: Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:

x = 0
while x <= 10:
    if x % 2 != 0:
        print(x)
    x += 1

# Pregunta 3: Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea. Usa el esqueleto de abajo:

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

# Pregunta 4: Crea un programa con un bucle for y una sentencia continue. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla. Usa el esqueleto de abajo:

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

# Pregunta 5: ¿Cuál es la output del siguiente código?

n = 3
 
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

# 4 3 2 1
# Nota: Falle

# Pregunta 6: ¿Cuál es la output del siguiente código?

n = range(4)
 
for num in n:
    print(num - 1)
else:
    print(num)

# 3, 2, 1, 0
# Nota: falle

# Pregunta 7: ¿Cuál es la output del siguiente código?

for i in range(0, 6, 3):
    print(i)

# 3
# Nota: A medias, falle. 