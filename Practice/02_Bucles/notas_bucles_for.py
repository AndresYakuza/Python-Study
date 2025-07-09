# -----------------------------------------------
# 🌀 Notas sobre Bucles `for` en Python
# -----------------------------------------------

# En Python, otro tipo de bucle muy común es el bucle `for`.
# Este se usa principalmente cuando sabemos cuántas veces queremos que se repita algo.

# Ejemplo de estructura básica:
for i in range(100):
    # Aquí va el bloque de código que se ejecutará 100 veces
    # por ahora, usamos `pass` como marcador de posición.
    pass

# -----------------------------------------------
# 🔍 Explicación del bucle for
# -----------------------------------------------

# 1. La palabra reservada `for` inicia el bucle.
# 2. `i` es una variable de control que va cambiando de valor en cada iteración.
# 3. `in range(100)` genera una secuencia de números desde 0 hasta 99 (100 valores).
#    NOTA: range(n) genera números desde 0 hasta n-1.
# 4. El cuerpo del bucle se ejecuta una vez por cada valor de `i`.
# 5. `pass` es una instrucción que no hace nada. Se usa para indicar que
#    el cuerpo del bucle está vacío por ahora.

# -----------------------------------------------
# 🧠 Cuándo usar `for` en lugar de `while`
# -----------------------------------------------

# - Usa `for` cuando necesitas repetir algo un número conocido de veces.
# - Usa `while` cuando necesitas repetir algo hasta que se cumpla (o deje de cumplirse) una condición.

# -----------------------------------------------
# 💡 Ejemplos prácticos de uso de for con range
# -----------------------------------------------

# Imprimir los números del 0 al 9:
for i in range(10):
    print(i)

# Contar hacia atrás del 10 al 1:
for i in range(10, 0, -1):
    print(i)

# Iterar por los números pares del 0 al 18:
for i in range(0, 20, 2):
    print(i)

# -----------------------------------------------
# 📝 Notas adicionales
# -----------------------------------------------

# - `range(start, stop, step)` permite más control:
#   - start: número inicial (incluido)
#   - stop: número final (no incluido)
#   - step: incremento (puede ser negativo)

# - `for` también se puede usar para recorrer listas, cadenas, diccionarios, etc.
#   Verás más sobre eso cuando estudies estructuras de datos.

# -----------------------------------------------
