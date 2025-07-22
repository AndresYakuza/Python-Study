
# 3.6.6   LAB   Operaciones con listas: conceptos básicos
# Escenario
# Imagina una lista - no muy larga ni muy complicada, solo una lista simple que contiene algunos números enteros. Algunos de estos números pueden estar repetidos, y esta es la clave. No queremos ninguna repetición. Queremos que sean eliminados.

# Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista. El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.

# Nota: Asume que la lista original está ya dentro del código - no tienes que ingresarla desde el teclado. Por supuesto, puedes mejorar el código y agregar una parte que pueda llevar a cabo una conversación con el usuario y obtener todos los datos.

# Sugerencia: Te recomendamos que crees una nueva lista como área de trabajo temporal - no necesitas actualizar la lista actual.

# No hemos proporcionado datos de prueba, ya que sería demasiado fácil. Puedes usar nuestro esqueleto en su lugar.


my_list = []
new_list = []

count = 1
print('Digite los valores para la lista, en caso de terminar digite -1')

while True:
    try:
        valores_user = int(input(f'Valor {count}: '))
    except ValueError:
        print('Solo se permiten número enteros...')
        continue
    
    if valores_user == -1:
        break
    
    my_list.append(valores_user)
    count += 1
    
for i in my_list:
    if i not in new_list:
        new_list.append(i)
        
print("\nLa lista con los datos originales")
print(my_list)   
print("\nLa lista con elementos únicos:")
print(new_list)