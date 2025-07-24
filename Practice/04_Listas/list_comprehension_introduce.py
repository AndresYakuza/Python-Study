# 🔹 Nivel 1 – Básico
# Crea una lista con los primeros 10 números naturales al cubo.
# Salida esperada: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

cubos = [x ** 3  for x in range(10)]
print(cubos)

cubos  = []
for x in range(0, 10):
    x = x ** 3
    cubos.append(x)
print(cubos)

# Genera una lista con los números del 1 al 20 que sean múltiplos de 3.

lista = [x for x in range(1, 20) if x % 3 == 0]
print(lista) 

lista =  []
for x in range(1, 20):
    if x % 3 == 0:
        lista.append(x)
print(lista)

# Dada esta lista:

# precios = [100, 250, 300, 150]
# Usa comprensión de listas para agregar 19% de IVA a cada precio.

precios = [100, 250, 300, 150]
precios_iva = []
for x in precios:
    x = int(x * 0.19 + x)
    precios_iva.append(x)
print(precios_iva)

precios = [100, 250, 300, 150]
precios_iva = [int(x * 0.19 + x) for x in precios]
print(precios_iva)

# De la lista:

# palabras = ["perro", "gato", "pez", "elefante"]
# Extrae solo las palabras que tengan más de 4 letras.

palabras = ["perro", "gato", "pez", "elefante"]
palabras1 = []
for x in palabras:
    if len(x) > 4:
        palabras1.append(x)
print(palabras1)

palabras = ["perro", "gato", "pez", "elefante"]
palabras_extraidas = [x for x in palabras if len(x) > 4]
print(palabras_extraidas)

# 🔸 Nivel 2 – Intermedio
# Dada una cadena, genera una lista con solo las vocales:

# texto = "Python es divertido"
# Resultado: ['o', 'e', 'u', 'i', 'o']
texto = "Python es divertido".lower()
abc = ['a', 'e', 'i', 'o', 'u']
resultado = []
for x in texto:
    
    if x in abc:
        resultado.append(x)
print(resultado)

texto = "Python es divertido".lower()
abc = ['a', 'e', 'i', 'o', 'u']
resultado = [x for x in texto if x in abc]
print(resultado)

# Dado un string:
# frase = "Hola Mundo"
# Obtén una lista con las letras convertidas a código ASCII (ord(letra)).

frase = "Hola Mundo"
resul =  [ord(x) for x in frase]

for x in frase:
    x = ord(x)
    resul.append(x)
print(resul)

# Crea una lista de todos los números entre 1 y 100 que no sean divisibles ni por 3 ni por 5.

numeros = []
for x in range(1, 100):
    if x % 3 != 0 and x % 5 != 0:
        numeros.append(x)

numeros = [x for x in range(100) if x % 3 != 0 and x % 5 != 0]
print(numeros)

# 🔥 Nivel 3 – Avanzado
# Matriz 3x3 con números del 1 al 9 (listas anidadas con comprensión):
# Resultado:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

matriz = [[i + j*3 for i in range(1, 4)] for j in range(3)]

for fila in matriz:
    print(fila)
    
# De la matriz anterior, crea una nueva con solo los valores pares, los impares deben ir como None.

matriz = [[i + j*3 for i in range(1, 4)] for j in range(3)]

matriz_pares = [
    [x if x % 2 == 0 else None for x in fila]
    for fila in matriz
]
for fila in matriz:
    print(fila)
    
for fila in matriz_pares:
    print(fila)

# A partir de una lista de nombres:

# nombres = ["Ana", "Pedro", "María", "juan", "Álvaro"]
# Crea una lista con solo los nombres que empiezan con letra mayúscula.

nombres = ["Ana", "Pedro", "María", "juan", "Álvaro"]
nombres_condicionales = [x for x in nombres if x == x.capitalize()]
print(nombres_condicionales)



