# Descripción: Este script recibe una lista de números enteros y devuelve la cantidad de números faltantes para hacer la secuencia consecutiva.
# Una secuencia consecutiva es una secuencia de números enteros en la que cada número es 1 unidad mayor que el anterior.
# Por ejemplo, [4, 8, 6] no es consecutivo porque falta el número 5 y 7.
# El script ordena la lista de números y calcula la diferencia entre el número más alto y el más bajo.
# Luego, calcula la cantidad de números faltantes entre el mínimo y el máximo para hacer la secuencia consecutiva.

def consecutivo(arr):
    # Ordenar el array para que los números estén en orden ascendente
    arr.sort()

    # Calcular la diferencia entre el número más alto y el más bajo
    rango = arr[-1] - arr[0]

    # Calcular la cantidad de números faltantes entre el mínimo y el máximo
    faltantes = rango - (len(arr) - 1)

    # Devolver el número de elementos faltantes para hacer la secuencia consecutiva
    return faltantes

# Ejemplos de uso:
print(consecutivo([4, 8, 6]))  # Devuelve 2 (agregar 5 y 7)
print(consecutivo([1, 2, 3, 5, 6]))  # Devuelve 1 (agregar 4)
print(consecutivo([10, -2, 3]))  # Devuelve 12 (agregar los números entre -2 y 10)