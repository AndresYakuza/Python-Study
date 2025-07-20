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
excelentes = []

for nombre, puntos, años, ausencias in empleados:

    # Si tiene advertencia, va solo ahí
    if puntos < 60 or ausencias > 10:
        advertencia.append(nombre)
        continue  # Evita que entre a las otras categorías

    # Si califica a ambas, va a "excelentes"
    if puntos >= 90 and años >= 3 and ausencias <= 2 and puntos >= 70 and ausencias <= 5:
        excelentes.append(nombre)
    else:
        if puntos >= 70 and ausencias <= 5:
            bono_anual.append(nombre)
        if puntos >= 90 and años >= 3 and ausencias <= 2:
            candidato_ascenso.append(nombre)

# 🔽 Impresión organizada
def imprimir_categoria(titulo, lista):
    print(f'\n{titulo}:')
    if lista:
        for nombre in lista:
            print('-', nombre)
    else:
        print('Sin registro')

imprimir_categoria('🌟 Bono + Ascenso (Excelentes)', excelentes)
imprimir_categoria('⚠️ Advertencia formal', advertencia)
imprimir_categoria('💰 Bono anual', bono_anual)
imprimir_categoria('📈 Candidatos a ascenso', candidato_ascenso)