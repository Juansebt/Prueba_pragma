# Descripción: Este script recibe una cadena de texto y devuelve el carácter o los caracteres que se deben eliminar para que la cadena sea un palíndromo.
# Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda.
# Ejemplo: "abjchba" se convierte en "abcba" eliminando los caracteres 'j' y 'c'.
# Si no es posible convertir la cadena en un palíndromo eliminando uno o dos caracteres, se devuelve un mensaje indicando que no es posible.

def crear_palindromo(cadena):
    # Convertir a minúsculas para una comparación insensible a mayúsculas
    cadena = cadena.lower()

    # Función auxiliar para verificar si una cadena es un palíndromo
    def es_palindromo(s):
        return s == s[::-1]

    # Iterar sobre la cadena, eliminando un carácter cada vez y verificando si es un palíndromo
    for i in range(len(cadena)):
        nueva_cadena = cadena[:i] + cadena[i + 1:]
        if es_palindromo(nueva_cadena) and len(nueva_cadena) >= 3:
            return f"'{cadena[i]}'"

    # Si no se encontró un palíndromo eliminando un carácter, intentar eliminando dos
    for i in range(len(cadena) - 1):
        for j in range(i + 1, len(cadena)):
            nueva_cadena = cadena[:i] + cadena[i + 1:j] + cadena[j + 1:]
            if es_palindromo(nueva_cadena) and len(nueva_cadena) >= 3:
                return f"'{cadena[i]}{cadena[j]}'"

    # Si no se encontró ningún palíndromo posible, devolver un mensaje
    return "No es posible."

# Ejemplo de uso:
print(crear_palindromo("abjchba"))  # "Se eliminaron los caracteres 'j' y 'c' para convertir la cadena en un palíndromo."
print(crear_palindromo("racecr"))   # "Se eliminó el carácter 'r' para convertir la cadena en un palíndromo."
print(crear_palindromo("abcde"))    # "No es posible crear un palíndromo eliminando 1 o 2 caracteres."