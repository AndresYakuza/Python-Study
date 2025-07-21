# 🧠 Reto del Día – Sistema de Trivia 🧠
# 🎯 Objetivo
# Simula un mini juego de preguntas y respuestas donde el usuario acumula puntos según sus respuestas correctas.

# 🧾 Reglas del reto:
# Hay una lista de preguntas con:

# Enunciado
# Opción correcta
# Puntos que otorga
# El usuario deberá ingresar su respuesta usando input().

# Si la respuesta es correcta:

# Se suma el puntaje.
# Si es incorrecta:
# No se suma nada.

# Al final, se imprime el puntaje total y un mensaje según su rendimiento.

# 📋 Datos de ejemplo:

# preguntas = [
#     ("¿Cuál es la capital de Francia?", "parís", 10),
#     ("¿Cuánto es 5 x 6?", "30", 5),
#     ("¿Cuál es el lenguaje que estás aprendiendo?", "python", 10),
#     ("¿Qué color resulta de mezclar rojo y azul?", "morado", 7)
# ]

# ✅ Tu tarea
# Recorre cada pregunta con un for.
# Usa input() para recibir la respuesta del usuario.
# Compara (ignorando mayúsculas/minúsculas).
# Suma el puntaje solo si responde bien.

# Al final, muestra:

# El puntaje total.

# Un mensaje como:
# 0 puntos → "No acertaste ninguna 😅"
# 1 o más → ""
# 30 o más → ""


preguntas = [
    ("¿Cuál es la capital de Francia?", "parís", 10),
    ("¿Cuánto es 5 x 6?", "30", 5),
    ("¿Cuál es el lenguaje que estás aprendiendo?", "python", 10),
    ("¿Qué color resulta de mezclar rojo y azul?", "morado", 7)
]
puntos_ganados = 0
num_pregunta = 1

for enunciado, opcion, puntos in preguntas:
    user_r = input(f'\nPregunta número {num_pregunta}: {enunciado}: ').strip().lower()
    num_pregunta += 1
    
    if user_r == opcion:
        puntos_ganados += puntos
        print("\n¡Correcto! Has ganado", puntos, "puntos.")
    else:
        print("\nIncorrecto. La respuesta correcta era:", opcion)
        
if puntos_ganados == 0:
    print('\n0 puntos → No acertaste ninguna 😅')
elif puntos_ganados < 30:
    print(f'\n{puntos_ganados} puntos → Buen intento 👍')
else:
    print(f'\n{puntos_ganados} puntos → ¡Excelente! 🧠')



