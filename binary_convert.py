# Descripción: Este script recibe una cadena binaria y la convierte a un número entero.
# La función recibe una cadena binaria y la convierte a un número entero.
# La función int() se utiliza para convertir la cadena binaria a un número entero.
# La función int() toma dos argumentos: la cadena binaria y la base 2.
# La base 2 indica que la cadena es un número binario.
# La función devuelve el número entero correspondiente a la cadena binaria.

def binary_convert(binary_str):
    # Usar int para convertir la cadena binaria a decimal
    return int(binary_str, 2)

# Ejemplos de uso:
print(binary_convert("1011"))  # Devuelve 11
print(binary_convert("1101"))  # Devuelve 13
print(binary_convert("1000"))  # Devuelve 8