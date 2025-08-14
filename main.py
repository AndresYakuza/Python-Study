
# def saludar(nombre):
#     print(f'Hola, {nombre}! Bienvenido.')
# saludar('Andrés')


# def cuadrado(numero):
#     print(f'El cuadrado de {numero} es: {numero * numero}')
# cuadrado(5)


# def operacion(a, b, tipo):
#     if tipo == 'suma':
#         print(f'La suma es: {a + b}')
#     elif tipo == 'resta':
#         print(f'La resta es: {a - b}')
#     elif tipo == 'multiplicacion':
#         print(f'La multiplicacion es: {a * b}')      
# operacion(2, 2, 'suma')
# operacion(2, 2, 'resta')
# operacion(2, 2, 'multiplicacion')


# def mostrar_datos(nombre, edad):
#     print(f'Nombre: {nombre}, Edad: {edad}')
# mostrar_datos('Andrés', 22)


# def celsius_a_fahrenheit(celsius):
#     print(celsius * 9/5 + 32)
# celsius_a_fahrenheit(100)


# def mensaje_personalizado(sujeto, accion, objeto):
#     print(f'{sujeto} {accion} {objeto}')
# mensaje_personalizado('Ana', 'está leyendo', 'un libro')


# def calculadora(a, b, operacion):
#     if operacion == 'suma':
#         print(f'La suma es: {a + b}')
#     elif operacion == 'resta':
#         print(f'La resta es: {a - b}')
#     elif operacion == 'multiplicacion':
#         print(f'La multiplicacion es: {a * b}')
#     elif operacion == 'division':
#         print(f'La divsión es: {a / b}')
#     else: 
#         print('Operación no reconocida.')  
# calculadora(2, 2, 'suma')
# calculadora(2, 2, 'resta')
# calculadora(2, 2, 'multiplicacion')
# calculadora(10, 2, 'division')
# calculadora(5, 9, 'raiz cuadrada')


# def ticket(producto, cantidad, precio_unitario):
#     print('Producto:', producto)
#     print('Cantidad:', cantidad)
#     print('Precio unitario:', precio_unitario)
#     print('Total:', cantidad * precio_unitario)

# ticket('Manzanas', 3, 2.5)

def sumas(a,b):
    return a + b
r = sumas(4, 4)
print(r)

def sumas(a,b):
    print(a + b)
sumas(4, 4)
