# -----------------------------------------------
# 🧠 Desafío: Quiz de Bucles en Python
# -----------------------------------------------

# Pregunta 1:
# ¿Cuál es la salida del siguiente código?

for i in range(2, 10, 2):
    print(i, end=' ')
# 2 4 6 8

# -----------------------------------------------

# Pregunta 2:
# ¿Cuál es la salida del siguiente código?

x = 5
while x > 0:
    x -= 1
    if x == 2:
        continue
    print(x, end=' ')

# 4 3 1 0 

# -----------------------------------------------

# Pregunta 3:
# ¿Qué imprime este programa?

for ch in "banana":
    if ch == "a":
        continue
    print(ch, end="")

# bnn

# -----------------------------------------------

# Pregunta 4:
# ¿Qué imprime este programa?

for ch in "pythonista":
    if ch == "t":
        break
    print(ch, end="")

# py

# -----------------------------------------------

# Pregunta 5:
# Crea un bucle `while` que cuente desde 10 hasta 1 (inclusive)
# e imprima solo los números pares.

# Escribe tu código aquí:
# while ...

x = 10
print(x)
while x > 1:
    x -= 1
    if x % 2 != 0:
        continue
    print(x)
print(x)


# x = 10
# while x >= 1:
#     if x % 2 == 0:
#         print(x)
#     x -= 1

# ❌ Pequeños errores:

# Estás imprimiendo x antes y después del bucle, lo cual repite el 10 y el 1 fuera de la lógica condicional.

# El resultado final incluye más de lo que se pide.

# -----------------------------------------------

# Pregunta 6:
# ¿Qué imprime este programa?

n = 1
while n < 5:
    print(n)
    n += 2
else:
    print("Fin")

# 1 3 fin

# -----------------------------------------------


# Pregunta 7:
# Corrige este código para que imprima los números del 1 al 5 (inclusive)
# usando un bucle `for`:

for i in range(1, 6):
    print(i)  # ← Este imprime del 1 al 4, ajústalo para incluir el 5
# -----------------------------------------------


# ✅ 6 / 7 → ¡APROBADO con nota alta!