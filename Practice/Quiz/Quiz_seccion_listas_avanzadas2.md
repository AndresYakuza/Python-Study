
# 🧠 Evaluación: Listas en Python – Preguntas y Retroalimentación

## ✅ Pregunta 1

```python
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)  # ➜ ['C']
```

**Respuesta:** ✅ `['C']`  
**Retroalimentación:** Todas las variables apuntan a la misma lista en memoria. El primer `del` elimina `"A"`, el segundo elimina `"B"`. Solo queda `"C"`.

---

## ✅ Pregunta 2

```python
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)  # ➜ ['B', 'C']
```

**Respuesta:** ✅ `['B', 'C']`  
**Retroalimentación:** Aunque `list_2` es eliminada, la lista sigue existiendo referenciada por `list_3`. Ya se había eliminado `"A"`.

---

## ✅ Pregunta 3

```python
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)  # ➜ []
```

**Respuesta:** ✅ `[]`  
**Retroalimentación:** El uso de `[:]` borra todos los elementos de la lista compartida. Así que `list_3` también queda vacía.

---

## ✅ Pregunta 4

```python
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)  # ➜ ['C']
```

**Respuesta:** ✅ `['C']`  
**Retroalimentación:** `list_2` y `list_3` son copias, no referencias. Por lo tanto, modificar una no afecta a la otra. `list_3` conserva todos sus elementos originales, excepto `"A"` que fue eliminado en `list_2`.

---

## ✅ Pregunta 5 – Operadores `in` y `not in`

```python
my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)           # ➜ True
print("A" not in my_list)     # ➜ True
print(3 not in my_list)       # ➜ True
print(False in my_list)       # ➜ False
```

**Respuestas:**
- ✅ `1 in my_list` → True (1 está en la lista)
- ✅ `"A" not in my_list"` → True ("A" como carácter no está)
- ✅ `3 not in my_list` → True (3 no está)
- ✅ `False in my_list` → False (False no está)

**Retroalimentación:** Uso correcto de los operadores `in` y `not in`. Recuerda que `"ABC"` **no contiene** `"A"` como elemento individual.

---

¡Buen trabajo! Has aplicado correctamente los conceptos de referencias, copias y operadores de pertenencia en listas.
