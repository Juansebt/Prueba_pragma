# Descripción: Este script calcula el número de minutos entre dos horas en un formato de 12 horas.
# La entrada es una cadena con las horas de inicio y fin separadas por un guion.
# Las horas están en el formato "hh:mm AM/PM".
# La salida es el número de minutos entre las dos horas.
# Ejemplo: "12:30 pm-12:00 am" devuelve 690 minutos (11 horas y 30 minutos).
# Si la hora de fin es antes de la hora de inicio, se asume que el rango de tiempo cruza la medianoche.
# En ese caso, la función calcula la diferencia de tiempo en consecuencia.

def count_minutes(time_range):
    # Función para convertir la hora en minutos
    def convert_to_minutes(time):
        # Separar el tiempo del período AM/PM
        time_part, period = time.split(' ')
        # Separar horas y minutos
        hours, minutes = map(int, time_part.split(':'))

        # Ajustar las horas según AM/PM a formato de 24 horas
        if period.lower() == 'pm' and hours != 12:
            hours += 12
        elif period.lower() == 'am' and hours == 12:
            hours = 0 

        # Devolver el total de minutos
        return hours * 60 + minutes

    # Separar el rango de tiempo en tiempo de inicio y fin
    start_time, end_time = time_range.split('-')
    # Convertir los tiempos a minutos
    start_minutes = convert_to_minutes(start_time)
    # Si el tiempo de fin es menor al de inicio, sumar 24 horas
    end_minutes = convert_to_minutes(end_time)

    # Si la hora de fin es menor que la de inicio, significa que pasa por medianoche
    if end_minutes < start_minutes:
        end_minutes += 24 * 60 # Añadir 24 horas en minutos

    # Devolver la diferencia en minutos
    return end_minutes - start_minutes

# Usage examples:
print(count_minutes("12:30 pm-12:00 am"))  # 690 minutes (11 hours and 30 minutes)
print(count_minutes("1:45 pm-3:15 pm"))    # 90 minutes (1 hour and 30 minutes)
print(count_minutes("11:30 pm-1:00 am"))   # 90 minutes (1 hour and 30 minutes)