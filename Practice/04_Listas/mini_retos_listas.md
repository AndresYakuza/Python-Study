
# 🧪 Mini Retos Avanzados – Listas en Python

## 🔢 1. Agrega elementos con `append` y `insert`

```python
# Crea una lista vacía e inserta:
# - El número 5 al final
# - El número 3 al inicio
# - El número 9 en la segunda posición

lista = []
lista.append(5)
lista.insert(0, 3)
lista.insert(1, 9)

print(lista)  # Resultado esperado: [3, 9, 5]
```

---

## 🔁 2. Combina listas

```python
# Une estas dos listas sin usar ciclos:

a = [1, 2, 3]
b = [4, 5, 6]
combinada = a + b

print(combinada)  # ➜ [1, 2, 3, 4, 5, 6]
```

---

## ❌ 3. Elimina por valor

```python
# De la lista, elimina solo la primera aparición del número 4

lista = [4, 2, 4, 1, 4]
lista.remove(4) 

print(lista)  # ➜ [2, 4, 1, 4]
```

---

## 🔄 4. Inversión de listas sin `.reverse()`

```python
# Invierte esta lista sin usar reverse()

original = [1, 3, 5, 7]
invertida = original[::-1]

print(invertida)  # ➜ [7, 5, 3, 1]
```

---

## 📚 5. Recorre y suma

```python
# Suma todos los elementos de la lista usando un for

numeros = [4, 1, 7, 2]
suma_total = 0

for i in numeros:
    suma_total += i

print(suma_total)  # ➜ 14
```

---

## 🧮 6. Lista por comprensión

> 💡 *List comprehension* es una forma compacta de crear listas en una sola línea usando una expresión y un bucle.

```python
# Crea una lista con los cuadrados de los números del 1 al 5 usando list comprehension

cuadrados = [i**2 for i in range(1, 6)]
print(cuadrados)  # ➜ [1, 4, 9, 16, 25]
```

---

## 🧼 7. Filtra elementos pares

```python
# Crea una nueva lista solo con los números pares

valores = [1, 2, 3, 4, 5, 6]
pares = [i for i in valores if i % 2 == 0]

print(pares)  # ➜ [2, 4, 6]
```

---

## 🎲 8. Doble condición con comprensión

```python
# Genera una lista con los múltiplos de 3 entre 1 y 30, pero que no sean múltiplos de 5

multiples = [i for i in range(1, 31) if i % 3 == 0 and i % 5 != 0]
print(multiples)  # ➜ [3, 6, 9, 12, 18, 21, 24, 27]
```

---

## 🔢 9. ¿Cuántas veces aparece?

```python
# Cuenta cuántas veces aparece el número 2

valores = [2, 4, 2, 6, 2, 8]
contador = valores.count(2)  # También puede hacerse con un bucle

print(contador)  # ➜ 3
```

---

## 🥇 10. Encuentra el mayor sin usar max()

```python
# Encuentra el valor más alto de la lista sin usar max()

datos = [23, 89, 15, 92, 5]
mayor = datos[0]

for i in datos:
    if i > mayor:
        mayor = i

print(mayor)  # ➜ 92
```
