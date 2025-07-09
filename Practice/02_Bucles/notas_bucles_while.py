# -----------------------------------------------
# 🔁 Notas sobre Bucles `while` en Python
# -----------------------------------------------

### 🧠 ¿Qué es un bucle while?

# El bucle `while` ejecuta una instrucción o un conjunto de instrucciones 
# **mientras** se cumpla una condición booleana (es decir, mientras sea True).

# Estructura general:
# while <condición>:
#     instrucción(es)

# Ejemplo básico:
contador = 0
while contador < 5:
    print(f"Valor actual: {contador}")
    contador += 1

# -----------------------------------------------
# 🧠 Cómo funciona:

# 1. La condición se evalúa antes de cada repetición.
# 2. Si es True, el cuerpo del bucle se ejecuta.
# 3. Al terminar una vuelta (iteración), se vuelve a evaluar la condición.
# 4. El bucle continúa hasta que la condición sea False.

# -----------------------------------------------
# ⚠️ ¡Precaución!

# Si la condición nunca se vuelve falsa, el bucle se convierte en infinito:
# Ejemplo (no ejecutar sin control):
# while True:
#     print("Esto nunca se detiene")

# Asegúrate de que la condición cambie dentro del bucle, para evitar bucles infinitos.

# -----------------------------------------------
# 💡 Cuándo usar while:

# - Cuando no sabes exactamente cuántas veces necesitas repetir algo.
# - Cuando depende de una condición que se puede cumplir en cualquier momento.
# - Cuando esperas a que algo suceda (por ejemplo, entrada del usuario, evento, etc.).

# -----------------------------------------------
# 🧪 Ejemplo realista:

respuesta = ""
while respuesta != "salir":
    respuesta = input("Escribe 'salir' para terminar: ")
    print("Dijiste:", respuesta)

# -----------------------------------------------
# 📝 Diferencias clave con for:

# - `while` se basa en una **condición lógica**.
# - `for` se basa en una **secuencia finita o rango predefinido**.

# Ambos son útiles, pero para diferentes situaciones.

# -----------------------------------------------
