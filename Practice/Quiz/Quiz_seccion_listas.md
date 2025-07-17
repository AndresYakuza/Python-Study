# 3.4.13 QUIZ DE SECCIÓN

# Pregunta 1: ¿Cuál es el resultado del siguiente fragmento de código?
# lst = [1, 2, 3, 4, 5]
# lst.insert(1, 6)
# del lst[0]
# lst.append(1)
 
# print(lst)

# Resultado
lst = [6, 2, 3, 4, 5, 1]
 

# Pregunta 2: ¿Cuál es el resultado del siguiente fragmento de código?
# lst = [1, 2, 3, 4, 5]
# lst_2 = []
# add = 0
 
# for number in lst:
#     add += number
#     lst_2.append(add)
 
# print(lst_2)

# Resultado
1, 3, 6, 10, 15
 

# Pregunta 3: ¿Cuál es el resultado del siguiente fragmento de código?
# omg = []
# del omg
# print(omg)

# Resultado 
# []
# Error, no importa si hay una lista vacia o con datos, del omg, elimina por completo la variable, por ende el resultado seria el siguiente:
# NameError: name 'lst' is not defined
 

# Pregunta 4: ¿Cuál es el resultado del siguiente fragmento de código?
# lst = [1, [2, 3], 4]
# print(lst[1])
# print(len(lst))

#Resultado
[2, 3]
3