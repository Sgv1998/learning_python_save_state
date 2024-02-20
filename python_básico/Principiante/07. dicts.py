### Dictionaries ###

# Definición
"""Un diccionario es una COLECCION de pares CLAVE-VALOR (key, value), donde cada clave debe ser única. 
Permite acceder a los valores a través de sus claves. Se definen utilizando llaves {} y los pares clave-valor 
se separan con dos puntos :. Los valores pueden ser de cualquier tipo."""
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)


print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1])   #No funciona la busqueda por índice, y en su lugar a buscado la key = "1"
print(my_dict["Nombre"])
print(my_dict.get("Edad"));  print("Esto es un get,    gracias a él podemos coger los VALUES de esa KEY")
print(type(my_dict.get("Edad")))

print("Moure" in my_dict)
print("Apellido" in my_dict)

# Inserción (de una Key nueva)
print("\t Inserción (de una Key nueva)")   # Es para no perderme en que parte de la leccion estamos
my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

# Actualización/modificación (de un Value)
print("\t Actualización")
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación
del my_dict["Calle"]
print(my_dict)

# Otras operaciones
print("Otras operaciones") 

print(my_dict.items())
print(my_dict.keys())  #Las palabras clave de los campos.
print(my_dict.values()) #Los valores que contienen las palabras clave

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))    #se generan esas KEYS
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))   
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev")   #Aquí se ha metido el VALUE mouredev en todas las Keys tomadas de my_dict.
print((my_new_dict))

# Imprimir KEYS
print(my_new_dict.keys())

for KEYS_ in my_new_dict.keys():
    print("Key-->", KEYS_)

# Imprimir VALUES
print(my_new_dict.values()) 

for VALUES_ in my_new_dict.values():
    print("valores-->", VALUES_)

# Moure queria mirar su type xd    
my_values = my_new_dict.values()
print(type(my_values))
 

# Imprimir Keys y Values:
for KeY,VaLuE in my_new_dict.items():
    print(KeY,VaLuE)



print("this is a list xd", list(dict.fromkeys(list(my_new_dict.values())).keys()))
print("this is a tuple xd", tuple(my_new_dict))
print("this is a set xd", set(my_new_dict))