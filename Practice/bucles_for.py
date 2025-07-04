

# Bucles en tu código con for

# Otro tipo de bucle disponible en Python proviene de la observación de que a veces es más importante contar los "giros o vueltas" del bucle que verificar las condiciones.

# for i in range(100):
#     # do_something()
#     pass

# la palabra reservada for abre el bucle for; nota - No hay condición después de eso; no tienes que pensar en las condiciones, ya que se verifican internamente, sin ninguna intervención.

# la función range() (esta es una función muy especial) es responsable de generar todos los valores deseados de la variable de control; en nuestro ejemplo, la función creará (incluso podemos decir que alimentará el bucle con) valores subsiguientes del siguiente conjunto: 0, 1, 2 .. 97, 98, 99; nota: en este caso, la función range() comienza su trabajo desde 0 y lo finaliza un paso (un número entero) antes del valor de su argumento.

# # nota la palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto; es una instrucción vacía - la colocamos aquí porque la sintaxis del bucle for exige al menos una instrucción dentro del cuerpo (por cierto - if, elif, else y while expresan lo mismo).

# ==== IMPORTANTE ===== 

# La función range() puede recibir entre 1 y 3 argumentos:

# range(inicio, fin, paso)
# inicio: desde dónde empieza 
# fin: hasta dónde va 
# paso: de cuánto en cuánto avanza (por defecto es 1)