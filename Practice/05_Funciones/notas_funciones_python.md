
# 🧠 Notas de Estudio: Funciones en Python

## 📌 ¿Qué es una función?

Una **función** es un bloque de código reutilizable que realiza una tarea específica. Se define una vez y puede ejecutarse muchas veces cuando se **invoca**.

Las funciones permiten:
- Reutilizar código
- Mejorar la organización del programa
- Hacerlo más legible y modular

---

## 🔹 Tipos de funciones en Python

| Tipo                               | Descripción                                                                 | Ejemplo                         |
|------------------------------------|-----------------------------------------------------------------------------|---------------------------------|
| Funciones integradas               | Vienen con Python (`print()`, `len()`, `sum()`, etc.)                       | `print("Hola")`                |
| Funciones de módulos               | Vienen en bibliotecas preinstaladas o externas (se verá más adelante)       | `math.sqrt(16)`                |
| Funciones definidas por el usuario | Son creadas por ti o por otros programadores                                | `def saludar():` ...           |
| Funciones lambda                   | Funciones anónimas para operaciones simples (se verá más adelante)          | `lambda x: x+1`                |

---

## 🔸 ¿Cómo se define una función?

```python
def nombre_funcion(parámetros_opcionales):
    # cuerpo de la función
```

📍 Puedes definir funciones **sin parámetros**:

```python
def mensaje():
    print("Hola")

mensaje()  # Invocación
```

📍 O con **parámetros**:

```python
def saludar(nombre):
    print("Hola,", nombre)

nombre = input("Ingresa tu nombre: ")
saludar(nombre)
```

---

## 📥 Parámetros vs Argumentos

- **Parámetro**: Variable que se define en la función (`nombre`)
- **Argumento**: Valor que se pasa al llamar la función (`"Luis"`)

```python
def cuadrado(x):  # x es un parámetro
    return x * x

cuadrado(5)  # 5 es un argumento
```

---

## 🔁 Reutilización de funciones

Las funciones se pueden llamar múltiples veces desde distintos lugares del código:

```python
def saludar():
    print("Hola!")

saludar()
saludar()
```

---

## ✅ Ventajas de usar funciones

- Evitas duplicar código
- Facilitas mantenimiento y actualización
- Permiten dividir el problema en tareas pequeñas (modularidad)
- Puedes probar y depurar en partes más fácilmente

---

## 🔗 Recursos útiles

- [Documentación oficial de funciones integradas](https://docs.python.org/3/library/functions.html)
