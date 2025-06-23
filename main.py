#  🔸 Ejercicio 3: Pide un número al usuario e indica si:
# Es positivo
# Es negativo
# Es cero


valor1 = float(input('Valor numerico: '))

if valor1 < 0:
    print('Negativo')
elif valor1 == 0:
    print('Es cero')
else:
    print('Positivo')