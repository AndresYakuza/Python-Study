# # # # lista_cuadrado = [x**2 for x in range(1,10)]
# # # # print(lista_cuadrado)

# # # # numeros_imapres = [x for x in range(1, 20) if x % 2 != 0]
# # # # print(numeros_imapres)

# # # elementos = ['casa', 'python', 'osos']
# # # convertidor = [x.upper() for x in elementos]
# # # print(convertidor)

# # multiplos_3 = [x for x in range(1, 31) if x % 3 == 0]
# # print(multiplos_3)

# elementos = ['casa', 'python', 'osos']
# palabras = [x for x in elementos if len(x) > 4]
# print(palabras)

# numeros = [2, 3, 4, -4, -12, -1]
# convertidor = [0 if x < 0 else x for x in numeros]
# print(convertidor)

# numeros = [f'{x} - par' if x % 2 == 0 else f'{x} - impar' for x in range(1, 11)]
# print(numeros)

# palabra = 'ciencia'
# caracteres_unicos = []
# caracteres = [caracteres_unicos.append(x) if x not in caracteres_unicos else x for x in palabra]
# print(caracteres_unicos)


# filas = 5
# columnas = 5
# row = [[x * columnas + j + 1 for j in range(columnas)] for x in range (filas)]
# for fila in row: 
#   print(fila)


# filas = 5
# columnas = 5
# row = [[x * columnas + j + 1 if j % 2 != 0 else "X" for j in range(columnas)] for x in range (filas)]
# for fila in row: 
#   print(fila)


# row =  [[j * x for j in range(1, 11)] for x in range(1, 11)]
# for f in row:
#     print(f)


# lista = ["hola", "mundo", "Python", "es", "genial"]
# vocales = 'aeiou'
# row = [sum(palabra.lower().count(v) for v in vocales) for palabra in lista]
# print(row)


