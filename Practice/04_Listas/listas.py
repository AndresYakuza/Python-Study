# # 🧠 Práctica con Listas en Python

# Una serie de ejercicios para ayudarte a dominar el uso de listas en Python. Están organizados por niveles de dificultad.

# ---

# ## ✅ Nivel Fácil

# ### 1. Crear y mostrar
# Crea una lista con los nombres de tus 3 comidas favoritas e imprímela.

comidas = ['Pastas con cerdo', 'Pastas con queso', 'Pastas con pollo']
print(f'Mis comidas favoritas son: {comidas}')

# ---

# ### 2. Reemplazar un elemento
# Crea una lista de 5 colores. Luego reemplaza el segundo color por otro que tú elijas.

colores = ['Red', 'Blue', 'Yellow', 'Rose', 'White']
print(f'Colores originales: {colores}')
colores[1] = 'Black'
print(f'Colores originales: {colores}')

# ---

# ### 3. Agregar elementos
# Crea una lista vacía y pide al usuario 3 números que se irán agregando con `append()`.

numeros = []

for i in range(1, 4):
    number = int(input(f'Digite el número {i}: '))
    numeros.append(number)
print(numeros)

# ---

# ### 4. Eliminar elementos
# Dada la lista:

# ```python
# nombres = ["Ana", "Luis", "Carlos", "Marta"]
# ```
# Elimina el nombre `"Luis"` usando `remove()` y muestra la nueva lista.

nombres = ["Ana", "Luis", "Carlos", "Marta"]
nombres.remove('Luis')
print(nombres)

# ---

# ## 🔷 Nivel Intermedio

# ### 5. Promedio de notas
# Pide al usuario 4 notas, guárdalas en una lista y luego calcula el promedio.

notas = []

for i in range(1, 5):

    user_notes = float(input(f'Digite la nota número {i}: '))
    notas.append(user_notes)

longitud = len(notas)
print(f'Notas: {notas}')
print(f'Promedio: {sum(notas)/longitud}')

# ---

# ### 6. Contar ocurrencias
# Dada la lista:

# ```python
# frutas = ["manzana", "pera", "manzana", "uva", "manzana"]
# ```

# Cuenta cuántas veces aparece `"manzana"` usando `.count()`.

# ---

# ### 7. Invertir la lista
# Pide al usuario que ingrese 5 números y luego muestra la lista invertida.

# ---

# ### 8. Máximo y mínimo
# Dada una lista de números:

# ```python
# [4, 7, 1, 3, 9, 2]
# ```

# Encuentra y muestra el valor **máximo** y **mínimo**.

# ---

# ## 🔶 Nivel Retador

# ### 9. Borrar todos los elementos
# Dada una lista cualquiera, vacíala completamente usando `.clear()`.

# ---

# ### 10. Adivina el número
# - Crea una lista con 5 números.
# - Pide al usuario un número y dile si está o no en la lista.

# Usa:

# ```python
# if numero in lista:
#     print("¡Sí está!")
# else:
#     print("No está en la lista.")
# ```

# ---

# 🧪 ¡Puedes mezclar varios conceptos para crear tus propios retos!