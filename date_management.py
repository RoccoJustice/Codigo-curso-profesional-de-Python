"""
import datetime

my_time = datetime.datetime.now() # El método now del módulo datetime me trae la fecha y hora de este momento en universal coordinated time (utc). Si mi computadora tiene una fecha, esto me va a traer la fehca y hora de mi configuración. SIn embargo, si no la tiene, como es el caso de un servidor, Python me trae la hora en utc.
print(my_time)

my_time = datetime.datetime.utcnow() # El método utcnow del módulo datetime me trae la fecha y hora de este momento en universal coordinated time (utc) si o si, sin importar la configuración de la hora de mi equipo.
print(my_time)

my_day = datetime.date.today() # Me trae solo la fecha de hoy

print(f'Year: {my_day.year}') # Me trae el año de mi fecha
print(f'Month: {my_day.month}') # Me trae el mes de mi fecha
print(f'Day: {my_day.day}') # Me trae el mes de mi fecha
"""

from datetime import datetime # para ya no tener que escribir datetime.datetime.xxx()

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(F'Formato LATAM: {my_str}')

my_str = my_datetime.strftime('%m/%d/%Y')
print(F'Formato USA: {my_str}')

my_str = my_datetime.strftime('Estamos en el año %Y')
print(F'Formato Random: {my_str}')