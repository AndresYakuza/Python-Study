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

👨‍💻 ¡Practica creando tus propias listas y experimentando con sus elementos!


