# Descripción: Este script recibe un número entero y verifica si está en la secuencia Fibonacci.
# La secuencia Fibonacci es una serie de números en la que cada número es la suma de los dos anteriores.
# Para verificar si un número está en la secuencia Fibonacci, se utiliza la fórmula de Binet.
# La función isPerfectSquare() verifica si un número es un cuadrado perfecto.
# La función esFibonacci() verifica si un número está en la secuencia Fibonacci.
# Si el número está en la secuencia Fibonacci, la función devuelve "Sí, está en la secuencia Fibonacci".
# De lo contrario, devuelve "NO".

import math

def FibonacciChecked(numero):
    def esFibonacci(num):
        return isPerfectSquare(5 * num * num + 4) or isPerfectSquare(5 * num * num - 4)

    def isPerfectSquare(x):
        s = math.isqrt(x)
        return s * s == x

    if esFibonacci(numero):
        return "Sí"
    else:
        return "NO"

# Ejemplos de uso:
print(FibonacciChecked(5))   # "Sí"
print(FibonacciChecked(7))   # "NO"
print(FibonacciChecked(13))  # "Sí"
print(FibonacciChecked(4))   # "NO"