
# ✅ Funciones y Métodos Comunes en Python

## 🔹 Funciones integradas en Python (Built-in Functions)

Estas funciones vienen incluidas con Python. Se llaman directamente con la sintaxis `función(valor)`.

| Función                     | ¿Qué hace?                                                                   | Ejemplo                          |
| --------------------------- | ---------------------------------------------------------------------------- | -------------------------------- |
| `max()`                     | Devuelve el valor **más grande** de varios valores o una colección           | `max(5, 10, 2)` → `10`           |
| `min()`                     | Devuelve el valor **más pequeño**                                            | `min(5, 10, 2)` → `2`            |
| `len()`                     | Devuelve la **cantidad de elementos**                                        | `len([1, 2, 3])` → `3`           |
| `sum()`                     | Suma todos los elementos numéricos de una lista                              | `sum([1, 2, 3])` → `6`           |
| `type()`                    | Devuelve el tipo de dato                                                     | `type("hola")` → `<class 'str'>` |
| `input()`                   | Permite al usuario ingresar datos desde teclado                              | `nombre = input("Tu nombre: ")`  |
| `int()`, `float()`, `str()` | Convierte entre tipos de datos                                               | `int("5")` → `5`                 |
| `range()`                   | Genera una secuencia de números                                              | `range(1, 5)` → `1, 2, 3, 4`     |
| `print()`                   | Muestra un valor en pantalla                                                 | `print("Hola")`                  |
| `abs()`                     | Devuelve el valor absoluto                                                   | `abs(-5)` → `5`                  |
| `round()`                   | Redondea un número                                                           | `round(3.1415, 2)` → `3.14`      |

---

## 🔹 Métodos comunes de listas (`list`)

Un **método** se aplica a un objeto específico, usando la sintaxis `objeto.metodo()`.

| Método         | ¿Qué hace?                                               | Ejemplo           |
| -------------- | -------------------------------------------------------- | ----------------- |
| `.append(x)`   | Agrega un elemento al final                              | `lista.append(5)` |
| `.pop()`       | Elimina y devuelve el último elemento (o por índice)     | `lista.pop()`     |
| `.remove(x)`   | Elimina la **primera** aparición del valor `x`           | `lista.remove(3)` |
| `.count(x)`    | Devuelve cuántas veces aparece `x`                       | `lista.count(2)`  |
| `.index(x)`    | Devuelve la posición del primer `x`                      | `lista.index(10)` |
| `.reverse()`   | Invierte el orden de los elementos                       | `lista.reverse()` |
| `.sort()`      | Ordena los elementos (menor a mayor)                     | `lista.sort()`    |
| `.insert(i, x)`| Inserta un valor `x` en la posición `i`                  | `lista.insert(1, 100)` |

---

## 🔹 Métodos comunes para cadenas (`str`)

| Método           | ¿Qué hace?                            | Ejemplo                                 |
| ---------------- | ------------------------------------- | --------------------------------------- |
| `.upper()`       | Convierte a mayúsculas                | `"hola".upper()` → `"HOLA"`             |
| `.lower()`       | Convierte a minúsculas                | `"HOLA".lower()` → `"hola"`             |
| `.capitalize()`  | Primera letra en mayúscula            | `"python".capitalize()` → `"Python"`    |
| `.strip()`       | Elimina espacios al principio y final | `" hola ".strip()` → `"hola"`           |
| `.replace(a, b)` | Cambia `a` por `b`                    | `"hola mundo".replace("hola", "adiós")` |
| `.count(x)`      | Cuenta cuántas veces aparece `x`      | `"banana".count("a")` → `3`             |
| `.find(x)`       | Devuelve la posición de `x`           | `"python".find("t")` → `2`              |
| `.startswith(x)` | Verifica si inicia con `x`            | `"python".startswith("py")` → `True`    |
| `.endswith(x)`   | Verifica si termina con `x`           | `"python".endswith("on")` → `True`      |
| `.split()`       | Divide la cadena en partes            | `"uno,dos".split(",")` → `["uno", "dos"]`|
| `.join(lista)`   | Une los elementos de una lista en un solo string | `",".join(["a","b"])` → `"a,b"`   |

---

## 🧠 Ejemplo de métodos en uso

```python
frutas = ["manzana", "pera", "manzana", "kiwi"]

print(frutas.count("manzana"))  # 2
frutas.append("naranja")
print(frutas)  # ['manzana', 'pera', 'manzana', 'kiwi', 'naranja']
frutas.reverse()
print(frutas)  # ['naranja', 'kiwi', 'manzana', 'pera', 'manzana']
```

---

## 📌 Notas útiles

- `input()` siempre devuelve un `str`. Para convertirlo a número usa `int()` o `float()`.
- `sort()` modifica la lista original. Si quieres una lista nueva ordenada, usa `sorted(lista)`.
- `find()` devuelve `-1` si no encuentra la subcadena.

---
