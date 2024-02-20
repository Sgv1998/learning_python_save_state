# Clase en vídeo: https://youtu.be/TbcEqkabAWU

### Dates ###

# Date time

from datetime import timedelta  # para operar con distintas fechas
from datetime import date       # agrupo fecha (año, mes, día)
from datetime import time       # agrupo hora (h, min, sec)
from datetime import datetime   # agrupo fecha y hora

now = datetime.now()


def print_date(fecha):
    print(fecha.year)
    print(fecha.month)
    print(fecha.day)
    print(fecha.hour)
    print(fecha.minute)
    print(fecha.second)
    print(fecha.timestamp)

print("now")
print_date(now)

year_2023 = datetime(2023, 1, 1)

print("year 2023")
print_date(year_2023)

# Time               # Es un objeto vacio, lo tienes que rellenar.


current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date


current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)        #Sí, este objeto lo volvera a usar despues, revalorizando su interior.

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)   #Aquí lo usa.

print(current_date.month)

# Operaciones con fechas            #Si los objetos son del mismo tipo, se pueden restar (dando los días restantes de una fecha a otra)

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date    #aqui year_2023 se está extrayendo su date para esta operación, porq el otro es un date.
print(diff)

# Timedelta         #esta hecho para trabajar con franjas de tiempo, en el que se define un espacio de tiempo que dura X.
                    # Si haces Ctr+click --> te dará mas info :) iras al módulo DATETIME en que se encuentra su código jajajaja. 
                    # En días, segundos, microseg, y el que quieras añadir (ej. weeks)
start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)