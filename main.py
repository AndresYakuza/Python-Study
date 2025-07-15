



# ### 5. Promedio de notas
# Pide al usuario 4 notas, guárdalas en una lista y luego calcula el promedio.

notas = []

for i in range(1, 5):

    user_notes = float(input(f'Digite la nota número {i}: '))
    notas.append(user_notes)

longitud = len(notas)
print(f'Notas: {notas}')
print(f'Promedio: {sum(notas)/longitud}')


