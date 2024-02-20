### Tuples ###

# Definición
"""Una tupla es una SECUENCIA INMUTABLE de elementos. Esto significa que, una vez creada, no se pueden modificar sus elementos. 
Se define utilizando paréntesis () y puede contener cualquier tipo de dato, incluso otras tuplas."""
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)
# Si solo tuvieras un elemnto, ponle una coma así --> tupla=(35 ,)

print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Brais"))
print(my_tuple.index("Moure"))
print(my_tuple.index("Brais"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas

print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined


# Crear una lista que solo incluya los numeros menores a 5
tuple=(13, 1, 8, 2, 3, 5, 8)

list=list()
for i in tuple:
    if i <=5: 
        list.append(i)
print("Estos son los números menores a 5 de tu lista: \n", list)