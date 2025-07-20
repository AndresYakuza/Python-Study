# 💡 Reto del Día – Clasificación de Tareas Pendientes 🗂️
# 🎯 Objetivo
# A partir de una lista de tareas con:

# descripción
# prioridad (alta, media, baja)
# estado (pendiente, en progreso, completada)

# ... tu tarea es clasificarlas y organizarlas por categoría.

# 🧾 Reglas
# Debes colocar cada tarea en una de las siguientes listas:

# Categoría	Condición
# 🟥 Urgente y pendiente	prioridad = "alta" y estado = "pendiente"
# 🟨 En progreso	estado = "en progreso"
# 🟩 Completadas	estado = "completada"
# 🟦 Pendientes no urgentes	estado = "pendiente" y prioridad es "media" o "baja"

# Una tarea solo puede pertenecer a una categoría.

# 📝 Datos de ejemplo:

# tareas = [
#     ("Preparar informe mensual", "alta", "pendiente"),
#     ("Responder correos", "media", "pendiente"),
#     ("Actualizar sitio web", "alta", "en progreso"),
#     ("Hacer copia de seguridad", "baja", "completada"),
#     ("Llamar al cliente", "alta", "completada"),
#     ("Organizar escritorio", "baja", "pendiente"),
#     ("Diseñar nueva propuesta", "alta", "pendiente")
# ]
# 🛠️ Tu misión
# Clasifica las tareas en 4 listas:

# urgente_pendiente
# en_progreso
# completadas
# pendientes_no_urgentes

# Imprime cada categoría con sus tareas.

# 🧠 Recomendaciones
# Usa for, if, elif, continue, como ya lo vienes haciendo.
# Puedes usar una función para imprimir las listas si lo deseas.
# Recuerda que una tarea debe ir solo a una categoría, en orden de prioridad.



tareas = [
    ("Preparar informe mensual", "alta", "pendiente"),
    ("Responder correos", "media", "pendiente"),
    ("Actualizar sitio web", "alta", "en progreso"),
    ("Hacer copia de seguridad", "baja", "completada"),
    ("Llamar al cliente", "alta", "completada"),
    ("Organizar escritorio", "baja", "pendiente"),
    ("Diseñar nueva propuesta", "alta", "pendiente"),
    ("", "alta", "pendiente"),
    ("Programar video juegos", "", "pendiente"),
    ("Escuchar musica", "esta en alta", "pendiente"),
    ("Armar una pc gamer", "alta", "566")
]

completadas = []
en_progreso = []
urgente_pendiente = []
pendientes_no_urgentes = []
incoherencia = []

for descripcion, prioridad, estado in tareas: 
    if estado.lower() == 'completada':
        completadas.append(descripcion)
        continue
    
    if estado.lower() == 'en progreso':
        en_progreso.append(descripcion)
        continue
    if descripcion.lower() == '' or prioridad.lower() == '' or estado.lower() == '':
        incoherencia.append((descripcion, prioridad, estado))
    elif estado.lower() == 'pendiente' and prioridad.lower() == 'alta':
        urgente_pendiente.append((descripcion, prioridad))
    elif estado.lower() == 'pendiente' and (prioridad.lower() == 'media' or prioridad.lower() == 'baja'):
        pendientes_no_urgentes.append((descripcion, prioridad))
    else:
        incoherencia.append((descripcion, prioridad, estado))
        
def imprimir_datos(titulo, lista):
    print(f'\n{titulo}:')
    if lista:
        for tarea in lista:
            print(f'\n- {tarea}')
    else:
        print('Sin registros...')
        
        
def imprimir_datos_tuplas_dobles(titulo, lista):
    print(f'\n{titulo}:')
    if lista:
        for tarea, prioridad in lista:
            print(f'\n- {tarea} \n - estado: {prioridad}')
    else:
        print('Sin registros...')
        
def imprimir_datos_tuplas_triples(titulo, lista):
    print(f'\n{titulo}:')
    if lista:
        for tarea, prioridad, estado in lista:
            print(f'\n»»» Tarea: {tarea} \n- prioridad: {prioridad} \n- estado: {estado}')
    else:
        print('Sin registros...')
            
 
imprimir_datos('🟩Tareas completadas', completadas)
imprimir_datos('🟨 Tareas en progreso', en_progreso)
imprimir_datos_tuplas_dobles('🟥 Tareas pendientes y urgentes', urgente_pendiente)
imprimir_datos_tuplas_dobles('🟦 Tareas pendiente y no urgentes', pendientes_no_urgentes)
imprimir_datos_tuplas_triples('Datos incoherentes o vacios', incoherencia)

 
    
    



