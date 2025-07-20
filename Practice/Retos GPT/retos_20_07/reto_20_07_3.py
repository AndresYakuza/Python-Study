# 📦 Reto del Día: Control de stock en bodega
# 🎯 Objetivo
# A partir de una lista de productos con su nombre, cantidad en inventario y stock mínimo, determina:

# ✅ Categorizaciones:
# Categoría	Condición
# 🟢 Stock suficiente	cantidad ≥ stock mínimo + 10 unidades
# 🟡 Reposición próxima	cantidad ≥ stock mínimo pero < mínimo + 10
# 🔴 Stock crítico	cantidad < stock mínimo
# ❌ Fuera de inventario	cantidad = 0

# 📋 Datos de ejemplo:
# inventario = [
#     ("Papel A4", 150, 100),
#     ("Tinta negra", 9, 15),
#     ("Resma reciclada", 0, 30),
#     ("Cuadernos", 60, 50),
#     ("Bolígrafos", 12, 10),
#     ("Carpetas", 15, 15),
#     ("Tijeras", 5, 8)
# ]
# 🛠️ Tu tarea:
# Clasifica cada producto en una sola de las 4 listas:

# stock_suficiente
# reponer_pronto
# stock_critico
# fuera_inventario

# Imprime cada categoría con su contenido.

# Usa lo que ya sabes: for, if, elif, listas y condiciones.
# (Opcional: usa una función para imprimir como en el reto anterior.)

inventario = [
    ("Papel A4", 150, 100),
    ("Tinta negra", 9, 15),
    ("Resma reciclada", 0, 30),
    ("Cuadernos", 60, 50),
    ("Bolígrafos", 12, 10),
    ("Carpetas", 15, 15),
    ("Tijeras", 5, 8)
]

stock_suficiente = []
reponer_pronto = []
stock_critico = []
fuera_inventario = []

for nombre, cantidad_inventario, stock_min in inventario:
    
    if cantidad_inventario == 0:
        fuera_inventario.append(nombre)
        continue
    
    if cantidad_inventario >= stock_min + 10:
        stock_suficiente.append(nombre)
    elif cantidad_inventario >= stock_min and cantidad_inventario < stock_min + 10:
        total = stock_min + 10 - cantidad_inventario
        reponer_pronto.append((nombre, total))
    elif cantidad_inventario < stock_min:
        stock_critico.append(nombre)
       
def imprimir_datos(titulo, lista):
    print(f'\n{titulo}:')
    if lista:
        for x in lista:
            print('-', x)
    else:
        print('Sin registros...')
         
imprimir_datos('Productos con stock suficiente', stock_suficiente)
imprimir_datos('Productos en stock crítico', stock_critico)
imprimir_datos('Productos fuera del inventario', fuera_inventario)

print('\nProductos a reporner pronto: ')
for producto, cantidad in reponer_pronto:
    print(f'- {producto}. Cantidad a reponer: {cantidad}')