
# 🎯 Objetivo:
# Crear un programa que reciba una lista de estudiantes con sus calificaciones, filtre los aprobados y los clasifique por rendimiento.

# 🧾 Requisitos:
# Usa listas para representar a los estudiantes y sus calificaciones.
# Usa condicionales para determinar si un estudiante está aprobado (nota >= 60).
# Usa bucles (for o while) para recorrer la lista.
# Usa operadores lógicos para clasificar:
# Excelente (>= 90)
# Bueno (60–89)
# Reprobado (< 60)

estudiantes = [
    ("Ana", 95),
    ("Luis", 70),
    ("Pedro", 58),
    ("Carla", 88),
    ("Lucía", 45),
    ("Marco", 91)
]

aprobados = []
reprobados = []

for estudiante, nota in estudiantes:
    if nota >= 60:
        if 60 < nota < 89:
            aprobados.append((estudiante, 'Bueno'))
        elif nota >= 90:
            aprobados.append((estudiante, 'Excelente'))
    elif nota < 60:
        reprobados.append((estudiante, 'Reprobado'))
        
aprobados = dict(aprobados)
reprobados =dict(reprobados)  
  
# Mostrar resultados
print('\nEstudiantes aprobados:')
for nombre, nivel in aprobados.items():
    print(f'- {nombre}: {nivel}')

print('\nEstudiantes reprobados:')
for nombre, nivel in reprobados.items():
    print(f'- {nombre}: {nivel}')
    
# El método .items() en Python se utiliza con diccionarios (dict) y te devuelve una vista de pares clave-valor como tuplas.