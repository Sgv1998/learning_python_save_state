# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=2938

### Variables ###

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

print(my_string_variable, my_int_variable, my_bool_variable)

# Dotar a las variables de ciertas caracteristicas, ej. un 'int' convertirlo en un 'str'
my_int_variable = 5
print(my_int_variable)
my_int_to_str_variable = str(my_int_variable)   #este era una variable que tenia el valor 5.
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))
type(my_int_to_str_variable)

#algunas FUNCIONES DEL SISTEMA
    #Len --> length, va a contar caracteres, incluidos espacios
print(len(my_string_variable))
    #Podemos hacer concatenaciones.
print("length of", my_string_variable, "=", len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, 
      ". Mi edad es:", age,
      ". Y mi alias es:", alias)

# Inputs            corre la linea, te va a hacer gracia, puedes contestarle
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)         #ojo, como comparte nombre con la variable 'name' de la linea anterior, se va a SOBRESCRIBIR.
print(age)


# Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))


#    Declare your age as integer variable
print("My age is", 25)
print (type(25))
#    Declare your height as a float variable
print ("my high is ", 1.85, " cm")
print (type(1.85))
#    Declare a variable that store a complex number
complex = 1 + 1j
print(complex = 1 + 1j)
print (type(complex))
#    Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
h=input("high of the triangle")
b=input("base of the triangle")
area=0.5*h*b
print(area)
#    Enter base: 20
#    Enter height: 10
#    The area of the triangle is 100