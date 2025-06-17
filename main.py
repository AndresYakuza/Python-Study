
num1 = int(input("Digite el primer numero: "))

num2 = int(input("Digite el segundo numero: "))

num3 = int(input("Digite el tercer numero: "))

nummax = num1

if num2	> nummax:
    nummax = num2

if num3 > nummax:
    nummax = num3

print('El numero mayor es:', nummax)