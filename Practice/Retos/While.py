
### While ####

# En general, en Python, un bucle se puede representar de la siguiente manera:

# while
#     instruction


#   LAB   Adivina el número secreto
#  ==================   Escenario =================================

# Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada secret_number. Quiere que todos los que ejecutan su programa jueguen el juego Adivina el número secreto, y adivina qué número ha elegido para ellos. ¡Quiénes no adivinen el número quedarán atrapados en un bucle sin fin para siempre! Desafortunadamente, él no sabe cómo completar el código.

# Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

# pedirá al usuario que ingrese un número entero;
# utilizará un bucle while;
# comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente. Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."
# ¡El mago está contando contigo! No lo decepciones.

#   INFO EXTRA  
# Por cierto, observa la función print(). La forma en que lo hemos utilizado aquí se llama impresión multilínea. Puedes utilizar comillas triples para imprimir cadenas en varias líneas para facilitar la lectura del texto o crear un diseño especial basado en texto. Experimenta con ello.


secret_number = 777
intentos = 0

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

entrada = input('Digite un número entero: ')


# 🧠 ¿Qué hace .isdigit()?
# Devuelve True si todos los caracteres en el string son números del 0 al 9.
# Devuelve False si el usuario escribe letras, símbolos, espacios o cualquier cosa rara.

if entrada.isdigit():

    user_number = int(entrada)
    while user_number != secret_number:
        intentos += 1
        print(
    f"""
    +========================================+
    | "¡Ja, ja! ¡Estás atrapado en mi bucle!"|
    |  === Intentos fallidos: {intentos} === |
    +========================================+
    """)
    
        entrada = input('Digite un número entero nuevamente: ')
        if entrada.isdigit():
            user_number = int(entrada)
        else:
            print(
        """
        +=========================================+
        | "¡Error! - Tramposo, eso no es valido.."|
        +=========================================+
        """)
      
    else:
                print(
            """
            +=========================================+
            | "¡Bien hecho, muggle! Eres libre ahora."|
            +=========================================+
            """)
else:
            print(
        """
        +=========================================+
        | "¡Error! - Tramposo, eso no es valido.."|
        +=========================================+
        """)

### Nota
### Me sali un poco de la dinamica principal, comence a experimentar y adiccionar algunas mecanicas diferentes, pero puede mejorar. 
# Mas adelante cuando domines try/except si recuerdas esto, mejorar el codigo. 






    

