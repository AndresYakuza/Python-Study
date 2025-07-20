# 💥 Reto del Día – Nivel Intermedio: Sistema de bonificación y ascensos
# 🎯 Objetivo
# A partir de una lista de empleados con nombre, puntuación de desempeño (0-100), años en la empresa y días de ausencia en el año, determina:

# Quiénes reciben bono anual.
# Quiénes pasan al comité de ascensos.
# Quiénes obtienen una advertencia formal.

# 🧾 Reglas
# Categoría	Requisitos
# Bono anual	Desempeño ≥ 70 y Ausencias ≤ 5
# Candidato a ascenso	Desempeño ≥ 90 y Años ≥ 3 y Ausencias ≤ 2
# Advertencia formal	Desempeño < 60 o Ausencias > 10
# Un empleado puede calificar para ascenso y bono a la vez.

# La advertencia excluye cualquier otra categoría: si alguien cumple un criterio de advertencia, queda sólo ahí.

# 🗂️ Datos de ejemplo
# empleados = [
#     ("Sofía", 92, 4, 1),
#     ("Carlos", 78, 2, 4),
#     ("Valentina", 59, 5, 3),
#     ("Diego", 88, 6, 0),
#     ("Martín", 95, 1, 0),
#     ("Elena", 83, 3, 7),
#     ("Rosa", 67, 10, 12)
# ]
# Resultado esperado para los datos de ejemplo
# Bono anual: Carlos, Diego, Elena
# Candidatos a ascenso: Sofía
# Advertencia formal: Valentina (desempeño < 60), Rosa (ausencias > 10)

# 🛠️ Tu tarea
# Implementa un script que procese la lista empleados.
# Llena tres listas: bono, ascenso, advertencia.
# Imprime las tres categorías de forma clara (puedes usar el formato que prefieras).
# Bonus: exporta las tres listas a un archivo CSV o muestra una tabla bonita -¡lo que más te motive!

# ¡A programar! 🚀


empleados = [
    ("Sofía", 92, 4, 1),
    ("Carlos", 78, 2, 4),
    ("Valentina", 59, 5, 3),
    ("Diego", 88, 6, 0),
    ("Martín", 95, 1, 0),
    ("Elena", 83, 3, 7),
    ("Rosa", 67, 10, 12)
]

bono_anual = []
candidato_ascenso = []
advertencia = []
excelent = []

for nombre, puntos_desempeno, años, dias_ausencia in empleados:
    # Candidato a ascenso
    if puntos_desempeno >= 90 and años >= 3 and dias_ausencia <= 2:
        candidato_ascenso.append(nombre)
    # Bono anual
    if puntos_desempeno >= 70 and dias_ausencia <= 5:
        bono_anual.append(nombre)
    # Advertencia formal
    if puntos_desempeno < 60 or dias_ausencia > 10:
        advertencia.append(nombre)
    
    if nombre in advertencia:
        if nombre in bono_anual:
            bono_anual.remove(nombre)
        if nombre in candidato_ascenso:
            candidato_ascenso.remove(nombre)

    if nombre in bono_anual and nombre in candidato_ascenso:
        bono_anual.remove(nombre)
        candidato_ascenso.remove(nombre)
        excelent.append(nombre)

print(f'\nLas siguientes personas califican para un bono anual y son candidatos a ascenso:')
if excelent:
    for nombre in excelent:
        print('-', nombre)
else:
    print('Sin registro')
    
print(f'\nAdvertencia formal:')
if advertencia: 
    for nombre in advertencia:
        print('-', nombre)
else:
    print('Sin registro')

print(f'\nBono anual:')
if bono_anual:
    for nombre in bono_anual:
        print('-', nombre)
else:
    print('Sin registro')

print(f'\nCandidatos a ascenso:')
if candidato_ascenso:
    for nombre in candidato_ascenso:
        print('-', nombre)
else:
    print('Sin registro')
    


