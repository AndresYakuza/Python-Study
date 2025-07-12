# 🐍 Operadores Lógicos y Bit a Bit en Python

## 1. Operadores Lógicos en Python

Los **operadores lógicos** permiten combinar expresiones booleanas:

| Operador | Descripción | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `and`    | Verdadero si **ambos operandos** son verdaderos | `True and True` | `True` |
| `or`     | Verdadero si **al menos uno** es verdadero | `True or False` | `True` |
| `not`    | Invierte el valor booleano | `not True` | `False` |

📌 **Nota:** Se usan comúnmente en estructuras condicionales (`if`, `while`...).

---

## 2. Operadores Bit a Bit (Bitwise)

Los **operadores bit a bit** trabajan a nivel de bits individuales. Se utilizan para manipulación binaria de enteros.

### Valores de Ejemplo

```python
x = 15  # binario: 0000 1111
y = 16  # binario: 0001 0000
```

### Tabla de Operadores

| Operador | Descripción                     | Ejemplo        | Resultado Decimal | Resultado Binario   |
|----------|----------------------------------|----------------|-------------------|----------------------|
| `&`      | AND bit a bit                   | `x & y`        | `0`               | `0000 0000`          |
| `|`      | OR bit a bit                    | `x | y`        | `31`              | `0001 1111`          |
| `~`      | NOT bit a bit (inversión)       | `~x`           | `-16`             | `1111 0000`*         |
| `^`      | XOR bit a bit                   | `x ^ y`        | `31`              | `0001 1111`          |
| `>>`     | Desplazamiento a la derecha     | `y >> 1`       | `8`               | `0000 1000`          |
| `<<`     | Desplazamiento a la izquierda   | `y << 3`       | `128`             | `1000 0000`          |

🔎 * El operador `~x` devuelve el complemento a dos con signo, por eso `~15 = -16` en decimal.

---

## 🧠 Complemento a Dos

En Python (y otros lenguajes), los enteros se representan internamente en **complemento a dos**. Por eso:
- `~x` no es solo invertir los bits, sino `-(x + 1)`
- Ejemplo: `~15 = -(15 + 1) = -16`

---

## 🛠️ Ejemplo de Código

```python
x = 15
y = 16

print("x & y =", x & y)       # 0
print("x | y =", x | y)       # 31
print("~x =", ~x)             # -16
print("x ^ y =", x ^ y)       # 31
print("y >> 1 =", y >> 1)     # 8
print("y << 3 =", y << 3)     # 128
```