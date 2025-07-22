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