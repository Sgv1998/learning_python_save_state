### date ###

from datetime import datetime

now = datetime.now()
"""
print(now.hour)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
"""
print("hola")
print(now)

def print_datetime(now):
    print(now.hour)
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)

print_datetime(now)

timestamp = now.timestamp()
print (timestamp)     # --> 1701021485.920676 esto cambiará si lo vuelves a correr... por partes... porque todo junto no quiere el programa
# Timestamp. Es un formato estandar de datación usado en todas las bases de datos y programación.
# que indica el tiempo pasado desde 1970, 1 de enero a las 00.
# y que se usa en vez de la fecha por año, mes, día, hora .... que es bastante engorroso.

year_2023 = datetime(2023, 1, 1) # Necesita sí o sí, año, mes y día, para funcionar.
print("This is the year", year_2023)

### TIME ###
from datetime import time    # Es un objeto vacio, hay que lanzar operaciones para poder acceder a sus datos.
print("This is the current time")   # Es un objeto que hay que rellenar.
current_time =time()        
print(current_time); print(current_time.hour); print(current_time.minute); print(current_time.second) # Da 0

current_time_fil= time(21, 6, 0)
print(current_time); print(current_time_fil.hour); print(current_time_fil.minute); print(current_time_fil.second)

### DATE ###

from datetime import date