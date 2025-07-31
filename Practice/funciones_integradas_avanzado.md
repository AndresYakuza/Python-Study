
# ✅ Funciones y Métodos Comunes en Python (Actualizado)

## 🔹 Funciones integradas en Python (Built-in Functions)

Estas funciones vienen incluidas con Python y están siempre disponibles. Se llaman directamente con la sintaxis `función(valor)`.

| Función         | ¿Qué hace?                                                       | Ejemplo                          |
|-----------------|-------------------------------------------------------------------|----------------------------------|
| `abs()`         | Devuelve el valor absoluto de un número                          | `abs(-5)` → `5`                  |
| `all()`         | Retorna `True` si todos los elementos de un iterable son `True`  | `all([True, 1, "x"])` → `True`   |
| `any()`         | Retorna `True` si al menos un elemento del iterable es `True`    | `any([0, False, 5])` → `True`    |
| `ascii()`       | Retorna una versión escapada de una cadena                       | `ascii("ñ")` → `'\xf1'`         |
| `bin()`         | Convierte un número a binario                                     | `bin(10)` → `'0b1010'`           |
| `bool()`        | Convierte un valor a booleano (`True` o `False`)                 | `bool("")` → `False`             |
| `breakpoint()`  | Inserta un punto de depuración                                    | `breakpoint()`                   |
| `bytearray()`   | Retorna un arreglo mutable de bytes                               | `bytearray(3)` → `b'\x00\x00\x00'` |
| `bytes()`       | Retorna un objeto inmutable de bytes                              | `bytes(3)` → `b'\x00\x00\x00'` |
| `callable()`    | Verifica si un objeto es invocable                                | `callable(len)` → `True`         |
| `chr()`         | Retorna el carácter unicode correspondiente a un entero          | `chr(65)` → `'A'`                |
| `classmethod()` | Define un método de clase                                         | —                                |
| `compile()`     | Compila código fuente a un objeto ejecutable                      | —                                |
| `complex()`     | Crea un número complejo                                           | `complex(2, 3)` → `(2+3j)`       |
| `dict()`        | Crea un diccionario                                               | `dict(a=1, b=2)` → `{'a':1, 'b':2}` |
| `dir()`         | Lista los atributos de un objeto                                  | `dir([])`                        |
| `divmod()`      | Retorna el cociente y el residuo                                  | `divmod(10, 3)` → `(3, 1)`       |
| `enumerate()`   | Retorna índice y valor de un iterable                             | `enumerate(['a','b'])`           |
| `eval()`        | Evalúa una cadena como código Python                              | `eval("2+2")` → `4`              |
| `exec()`        | Ejecuta una cadena de código Python                               | `exec("a=5")`                    |
| `filter()`      | Filtra elementos usando una función                               | `filter(lambda x: x>0, [-1,2])`  |
| `float()`       | Convierte a número decimal                                        | `float("3.14")` → `3.14`         |
| `format()`      | Formatea cadenas o números                                        | `format(3.1415, ".2f")` → `'3.14'` |
| `frozenset()`   | Crea un conjunto inmutable                                        | `frozenset([1,2])`               |
| `getattr()`     | Obtiene el atributo de un objeto                                  | `getattr(obj, "x")`              |
| `globals()`     | Devuelve el diccionario global actual                             | `globals()`                      |
| `hasattr()`     | Verifica si un objeto tiene un atributo                           | `hasattr(obj, "x")`              |
| `hash()`        | Devuelve el valor hash de un objeto                               | `hash("hola")`                   |
| `help()`        | Muestra ayuda interactiva                                         | `help(print)`                    |
| `hex()`         | Convierte a hexadecimal                                           | `hex(255)` → `'0xff'`            |
| `id()`          | Devuelve el identificador de un objeto                            | `id("hola")`                     |
| `input()`       | Lee una entrada desde teclado                                     | `input("Nombre: ")`              |
| `int()`         | Convierte a entero                                                | `int("5")` → `5`                 |
| `isinstance()`  | Verifica si es instancia de un tipo                               | `isinstance(5, int)` → `True`    |
| `issubclass()`  | Verifica si una clase hereda de otra                              | `issubclass(bool, int)` → `True` |
| `iter()`        | Retorna un iterador                                                | `iter([1,2,3])`                  |
| `len()`         | Longitud de un iterable                                           | `len("hola")` → `4`              |
| `list()`        | Convierte a lista                                                 | `list("abc")` → `['a', 'b', 'c']`|
| `locals()`      | Muestra las variables locales                                     | `locals()`                       |
| `map()`         | Aplica función a cada elemento                                    | `map(str, [1,2])` → `['1', '2']` |
| `max()`         | Máximo valor de una colección                                     | `max([1, 5, 3])` → `5`           |
| `memoryview()`  | Crea una vista de memoria                                         | `memoryview(b'abcd')`            |
| `min()`         | Mínimo valor de una colección                                     | `min([1, 5, 3])` → `1`           |
| `next()`        | Devuelve el siguiente valor del iterador                          | `next(iter([10, 20]))` → `10`    |
| `object()`      | Retorna un objeto vacío                                           | `object()`                       |
| `oct()`         | Convierte a octal                                                 | `oct(8)` → `'0o10'`              |
| `open()`        | Abre un archivo                                                    | `open("archivo.txt")`            |
| `ord()`         | Retorna el código unicode de un carácter                          | `ord("A")` → `65`                |
| `pow()`         | Potenciación                                                      | `pow(2,3)` → `8`                 |
| `print()`       | Imprime en pantalla                                               | `print("Hola")`                  |
| `property()`    | Crea propiedades en clases                                        | —                                |
| `range()`       | Genera una secuencia de números                                   | `range(3)` → `0,1,2`             |
| `repr()`        | Representación oficial de un objeto                               | `repr("hi")` → `'hi'`            |
| `reversed()`    | Invierte un iterable                                              | `list(reversed([1,2,3]))`        |
| `round()`       | Redondea un número                                                | `round(3.14)` → `3`              |
| `set()`         | Crea un conjunto                                                  | `set([1,2,2])` → `{1, 2}`        |
| `setattr()`     | Asigna un atributo                                                | `setattr(obj, "x", 5)`           |
| `slice()`       | Objeto de corte                                                   | `slice(1,5)`                     |
| `sorted()`      | Retorna una lista ordenada                                        | `sorted([3,1,2])` → `[1,2,3]`     |
| `staticmethod()`| Define un método estático                                         | —                                |
| `str()`         | Convierte a cadena                                                | `str(5)` → `'5'`                 |
| `sum()`         | Suma los elementos de una colección                               | `sum([1,2,3])` → `6`             |
| `super()`       | Llama a la clase padre                                            | `super().metodo()`               |
| `tuple()`       | Crea una tupla                                                    | `tuple([1,2])` → `(1,2)`         |
| `type()`        | Tipo de un objeto                                                 | `type(5)` → `<class 'int'>`      |
| `vars()`        | Devuelve los atributos de un objeto                               | `vars(obj)`                      |
| `zip()`         | Combina iterables en tuplas                                       | `zip([1,2],["a","b"])` → `[(1,'a'),(2,'b')]` |
| `__import__()`  | Importación manual avanzada                                       | `__import__('math')`            |
