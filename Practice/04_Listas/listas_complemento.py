# 🧩 1. Eliminar duplicados sin usar set()
# Dada una lista con números repetidos, elimina los duplicados manteniendo el orden.
# numeros = [4, 2, 4, 7, 2, 9, 1, 4, 7]
# # Resultado esperado: [4, 2, 7, 9, 1]

numeros = [4, 2, 4, 7, 2, 9, 1, 4, 7]
new_numeros = []

for unidad in numeros:
    if unidad not in new_numeros:  # Si no está ya en la nueva lista
        new_numeros.append(unidad)  # Lo agregamos

print(new_numeros)  # [4, 2, 7, 9, 1]

# 🔁 2. Aplanar una lista de listas
# Convierte una lista anidada en una sola lista plana.
# listas = [[1, 2], [3, 4], [5, 6]]
# # Resultado esperado: [1, 2, 3, 4, 5, 6]


listas = [[1, 2], [3, 4], [5, 6]]
resultado = []

for unidad in listas:
    for unidad2 in unidad:
        resultado.append(unidad2)

print(resultado)

# 📊 3. Contar elementos únicos
# Dada una lista, cuenta cuántos elementos son únicos (es decir, que solo aparecen una vez).
# datos = [1, 2, 2, 3, 4, 4, 5]
# # Resultado esperado: 3 (los únicos son 1, 3, 5)

datos = [1, 2, 2, 3, 4, 4, 5]
valores_unicos = []


for unidad in datos:
    if datos.count(unidad) == 1: 
        valores_unicos.append(unidad)

print(f'Resultado esperado: {len(valores_unicos)} (los únicos son: {valores_unicos})')

# 📏 4. Longitud de palabras
# Dada una lista de palabras, crea una nueva lista con la longitud de cada palabra.
# palabras = ['python', 'listas', 'practica']
# # Resultado esperado: [6, 6, 8]


palabras = ['python', 'listas', 'practica']
longitud = []

for palabra in palabras:
    longitud.append(len(palabra))
print(longitud)

# 🔢 5. Pares e impares separados
# Dada una lista de números, separa los pares e impares en dos listas.
# numeros = [1, 4, 7, 8, 2, 5, 10]
# # pares = [4, 8, 2, 10], impares = [1, 7, 5]

numeros = [1, 4, 7, 8, 2, 5, 10]
pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'Pares = {pares}, impares = {impares}')


# ↕️ 6. Rotar elementos
# Rota los elementos de una lista una posición a la derecha.
# valores = [10, 20, 30, 40]
# # Resultado esperado: [40, 10, 20, 30]


valores = [10, 20, 30, 40]
valores = valores[-1:] + valores[:-1]
print(valores)


# 🔄 7. Intercambiar extremos
# Intercambia el primer y último elemento de la lista.
# lista = [1, 2, 3, 4, 5]
# # Resultado esperado: [5, 2, 3, 4, 1]

lista = [1, 2, 3, 4, 5]
lista = lista[-1:] + lista[1:-1] + lista[:1]
# lista[0], lista[-1] = lista[-1], lista[0] Otra opción. 
print(lista)

# 🧠 8. Sublistas crecientes
# Encuentra todas las sublistas crecientes dentro de una lista.
# lista = [1, 2, 1, 2, 3, 1]
# # Resultado esperado (sublistas crecientes consecutivas): [[1, 2], [1, 2, 3]]


lista = [1, 2, 1, 2, 3, 1]
sublistas_crecientes = []
sublista_actual = []

for i in range(len(lista)):
    if not sublista_actual:
        sublista_actual.append(lista[i])
    elif lista[i] > sublista_actual[-1]:
        sublista_actual.append(lista[i])
    else:
        if len(sublista_actual) > 1:
            sublistas_crecientes.append(sublista_actual)
        sublista_actual = [lista[i]]

# Verificamos al final por si la última sublista era creciente
if len(sublista_actual) > 1:
    sublistas_crecientes.append(sublista_actual)

print(sublistas_crecientes) 


# ♻️ 9. Eliminar elementos consecutivos duplicados
# Dada una lista, elimina los elementos duplicados solo si son consecutivos.
# datos = [1, 1, 2, 2, 2, 3, 1, 1, 4]
# # Resultado esperado: [1, 2, 3, 1, 4]


# 🧮 10. Suma acumulativa
# Transforma una lista en su forma acumulada.
# valores = [1, 2, 3, 4]
# # Resultado esperado: [1, 3, 6, 10]