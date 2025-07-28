🟢 NIVEL 1: BÁSICO
Crear una lista de los cuadrados de los números del 1 al 10.

Filtrar los números impares del 1 al 20.

Convertir todos los elementos de una lista de strings a mayúsculas.

Obtener una lista con los primeros 10 múltiplos de 3.

🟡 NIVEL 2: INTERMEDIO
De una lista de palabras, obtener las que tengan más de 4 letras.

Reemplazar los números negativos de una lista con 0.

Crear una lista de "par" o "impar" para los números del 1 al 10.

Obtener los caracteres únicos de una palabra (sin repetir).

🔴 NIVEL 3: AVANZADO
Crear una matriz 5x5 con valores del 1 al 25.

De una matriz dada, reemplazar los valores impares por "X" y los pares por el mismo valor.

Crear una tabla de multiplicar (del 1 al 10) usando listas anidadas.

Dada una lista de strings, crear otra lista con la cantidad de vocales en cada string.


🧩 AHORA SÍ: MINI RETO
🎯 Reto:
Genera una matriz 4×4 con números del 1 al 16, pero:

Si el número es divisible por 3, reemplázalo por "*"

Si no lo es, almacena el cuadrado del número

📝 Reglas:
Hazlo en una sola list comprehension anidada

Usa la fórmula i * columnas + j + 1 para calcular los números

filas = 4
columnas = 4
row = [[(x * columnas + j + 1) ** 2 if (x * columnas + j + 1) % 3 == 0 else "*" for j in range(columnas)]for x in range (filas)]
for fila in row: 
  print(fila)
