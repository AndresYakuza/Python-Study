
# 🧪 Ejercicios de Práctica – Listas Avanzadas en Python

## 🔁 1. ¿Alias o copia?
```python
a = [1, 2, 3]
b = a
a[0] = 99
print(b)  # ¿Qué imprime?
```
**Respuesta del usuario:** `[99, 2, 3]`  
✅ Correcto. Ambas variables apuntan a la **misma lista** (alias), así que cualquier cambio en `a` afecta a `b`.

---

## 📤 2. Crea una copia verdadera
```python
list_1 = [42]
list_2 = list_1
list_1[0] = 99
print(list_2)  # Debe seguir siendo [42]
```
**Respuesta del usuario:** `list_2 = list_1[:]`  
✅ Correcto. Usar slicing (`[:]`) crea una copia nueva e independiente de la original.

---

## 🔪 3. Rebanada de mitad a fin
```python
numbers = [10, 20, 30, 40, 50, 60]
mid = len(numbers) // 2
print(numbers[mid:])  # ¿Qué imprime?
```
**Respuesta del usuario:** `[40, 50, 60]`  
✅ Correcto. `mid` es `3`, así que el slicing empieza en `index 3` (40) hasta el final.

---

## 🔄 4. Índices negativos con paso invertido
```python
my_list = [0, 1, 2, 3, 4, 5, 6]
print(my_list[-1:2:-1])
print(my_list[-1:1:-1])  # ¿Qué pasa si cambias el 2 por 1?
```
**Respuesta del usuario:**  
- `[-1:2:-1]` da `[6, 5, 4, 3]`  
- `[-1:1:-1]` da `[6, 5, 4, 3, 2]`  
✅ Correcto. El segundo valor del slicing es el **límite que no se incluye**.

---

## ❌ 5. Usa del con rebanada
```python
my_list = [10, 20, 30, 40, 50]
del my_list[1:4]
print(my_list)
```
**Respuesta del usuario:** `Se eliminan todos excepto el primero (10)`  
✅ Correcto. Queda `[10, 50]`.

---

## 📭 6. Vacía la lista sin eliminarla
```python
my_list = [5, 10, 15, 20]
# Vacía la lista usando slicing
```
**Respuesta del usuario:** `my_list = my_list[4:]`  
⚠️ Funciona, pero lo ideal sería `my_list[:] = []` para mantener el objeto intacto si hay alias.

---

## 💥 7. Elimina la lista por completo
```python
my_list = [1, 2, 3]
del my_list
print(my_list)  # ¿Qué pasa?
```
**Respuesta del usuario:** `Error porque la variable ya no existe`  
✅ Correcto. Lanza `NameError` al intentar imprimir una variable eliminada.

---

## 🧪 Bonus Challenge: copia modificada
```python
original = [1, 2, 3, 4, 5]
# Crear una copia invertida sin afectar la original
```
**Respuesta del usuario:**  
```python
original = original[-1::-1]
print(original)
```
⚠️ Casi. Eso invierte, pero **afecta a la original**.  
✅ Corrección:  
```python
copy_reversed = original[::-1]
print(copy_reversed)
```
