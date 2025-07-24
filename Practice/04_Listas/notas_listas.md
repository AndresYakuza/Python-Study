# 📘 Apuntes de Listas en Python

Las **listas** en Python son estructuras de datos que permiten almacenar múltiples elementos en un solo objeto. Son **mutables**, lo que significa que se pueden modificar después de haber sido creadas.

## 📌 Creación de una lista

```python
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)
```

Salida:
```
Contenido de la lista original: [10, 5, 7, 2, 1]
```

## 🔢 Indexación

Cada elemento en una lista tiene un **índice**, que comienza desde `0`:

| Índice | Elemento |
|--------|----------|
| 0      | 10       |
| 1      | 5        |
| 2      | 7        |
| 3      | 2        |
| 4      | 1        |

También se puede acceder a los elementos **desde el final**, usando índices negativos:

| Índice | Elemento |
|--------|----------|
| -1     | 1        |
| -2     | 2        |
| ...    | ...      |

### Acceso a un elemento:

```python
print(numbers[0])    # Primer elemento: 10
print(numbers[-1])   # Último elemento: 1
```

## 🧾 Modificación de elementos

Puedes modificar el valor de un elemento directamente usando su índice:

```python
numbers[0] = 111      # Cambiamos el primer elemento
numbers[1] = numbers[4]  # Copiamos el valor del último elemento al segundo
print("Nuevo contenido de la lista:", numbers)
```

Salida:
```
Nuevo contenido de la lista: [111, 1, 7, 2, 1]
```

## 📏 Longitud de la lista

Puedes obtener la cantidad de elementos con `len()`:

```python
print("Longitud de la lista:", len(numbers))  # 5
```

## ❌ Eliminación de elementos

Para eliminar un elemento de la lista, puedes usar `del` seguido del índice:

```python
del numbers[2]  # Elimina el tercer elemento (índice 2)
print(numbers)
```

Salida:
```
[111, 1, 2, 1]
```

## ✅ Resumen

- Las listas son mutables.
- Se accede a elementos por índice (`numbers[0]`) o desde el final (`numbers[-1]`).
- Puedes modificar, eliminar y consultar elementos.
- La función `len()` da la cantidad de elementos.
- `del` elimina elementos por índice.

---

## 🧠 Asignación de listas: alias vs copia

Cuando haces una asignación como:

```python
list_1 = [1]
list_2 = list_1
```

Ambas variables apuntan a la misma lista en memoria. Si modificas una, la otra también se ve afectada:

```python
list_1[0] = 2
print(list_2)  # ➜ [2]
```

✅ Copiar el contenido (no la referencia)  
Para crear una copia real, usa una rebanada completa:

```python
list_2 = list_1[:]
```

Así, modificar list_1 no afecta a list_2.

## 🍰 Rebanadas (slicing) avanzadas

```python
my_list[start:end]
```

* Incluye start, excluye end.
* Si start > end con paso positivo (+1), el resultado es una lista vacía.
* Puedes usar índices negativos para contar desde el final.

Ejemplos:

```python
my_list = [10, 8, 6, 4, 2]

my_list[1:-1]      # ➜ [8, 6, 4]
my_list[-1:1]      # ➜ []  (orden inválido con paso por defecto)
my_list[-1:1:-1]   # ➜ [2, 4, 6]  (paso negativo: va hacia atrás)
```

## 🗑️ Eliminación con del usando rebanadas

Eliminar una porción:

```python
del my_list[1:3]  # Elimina elementos en índices 1 y 2
```

Vaciar toda la lista (pero no eliminar la variable):

```python
del my_list[:]  # ➜ []
```

Eliminar completamente la lista:

```python
del my_list
print(my_list)  # ➜ Error: la variable ya no existe
```

## 🔍 Operadores `in` y `not in`

```python
elem in lista     # Devuelve True si elem está en la lista
elem not in lista # Devuelve True si elem NO está en la lista
```

✅ Ejemplo:
```python
my_list = [10, 20, 30]
print(20 in my_list)     # ➜ True
print(50 not in my_list) # ➜ True
```


# 🧠 Comprensión de listas (List Comprehension)

Una **list comprehension** es una forma concisa y elegante de crear listas aplicando una expresión sobre un iterable (como `range`, otra lista, etc.), con posibilidad de filtrar.

## 📌 Sintaxis básica

```python
[nueva_expresión for elemento in iterable if condición]
```

---

## ✅ Ejemplos:

```python
[x**2 for x in range(5)]               # ➜ [0, 1, 4, 9, 16]
[x for x in range(10) if x % 2 == 0]   # ➜ solo pares
[x.upper() for x in nombres]          # ➜ nombres en mayúscula
```

---

## 🧠 Regla de oro

### ✔️ `if` al **final** (sin `else`):
Sirve para **filtrar** elementos (los que no cumplen, se eliminan).
```python
[x for x in lista if x > 0]
```

### ✔️ `if...else` al **inicio**:
Sirve para **transformar cada elemento** según una condición (todos los elementos se mantienen, cambia su valor).
```python
["par" if x % 2 == 0 else "impar" for x in range(5)]
```

---

### ⚠️ Importante:
- No se puede usar `else` sin `if`.
- No puedes mezclar `if` final con `else` al inicio.

---

# 📐 Comprensión de listas anidadas (Matrices)

Una **matriz** es una lista que contiene otras listas. Ejemplo: un tablero 3x3:

```python
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
```

---

## ✅ Crear una matriz con comprensión anidada:

```python
# Matriz de 3x3 con valores del 1 al 9
matriz = [[i + j*3 for i in range(1, 4)] for j in range(3)]
```

---

## 🔁 Recorrer una matriz:

```python
for fila in matriz:
    for elemento in fila:
        print(elemento)
```

---

## 🎯 Ejemplo: matriz con valores pares o None

```python
matriz_pares = [
    [x if x % 2 == 0 else None for x in fila]
    for fila in matriz
]
```

---

## 🧊 Matrices más grandes (ejemplo práctico):

```python
# Temperaturas: 31 días, 24 horas por día
temps = [[0.0 for h in range(24)] for d in range(31)]
```

Puedes acceder a:
- Día 5, hora 12: `temps[4][11]`

---


