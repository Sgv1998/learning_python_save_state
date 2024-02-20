# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=26619

### Functions ###

# Definición

def my_function():
    print("Esto es una función")


my_function()
my_function()
my_function()

# Función con parámetros de entrada/argumentos


def sum_two_values(first_value=5, second_value=8):   #habia puesto first_value:int para explicar que el indicar que es un int es inutil, porque si metes un texto, se sobrescribira.--> python es de tipado debil recuerda
    print(first_value + second_value)                  # pero bueno, como ves, lo que pongAS LUEGO en ese parentesis afectará al valor de los objetos de la función.

sum_two_values()
sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno.
print("Funcion con parametros de entrada/argunmentos y retorno")

def sum_two_values_with_return(first_value, second_value):     #no dio resultados
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entrada/argumentos por clave.


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Moure", name="Brais")

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

# Función con parámetros de entrada/argumentos arbitrarios


def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")

### OTROS EJEMPLOS ###
print("### OTROS EJEMPLOS ###")

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print("Me llamo :", generate_full_name("Juan", "mustafar"))

def saludar(nombre):
    print("Hola, " + nombre)


## DIferencias entre usar return y no usarlo ##
resultado_saludo = saludar("Juan")
print(resultado_saludo)  # Esto imprimirá "Hola, Juan" seguido de "None"

def saludar_con_return(nombre):
    mensaje = "Hola, " + nombre
    return mensaje

resultado_saludo = saludar_con_return("Juan")
print(resultado_saludo)  # Esto imprimirá "Hola, Juan"

### En resumen, return es útil cuando deseas que una función devuelva un valor específico, y este valor puede ser utilizado de diversas
# formas, como asignándolo a una variable, utilizándolo en expresiones o pasándolo como argumento a otra función. Si una función no 
# utiliza return o si omite la palabra clave return, la función devuelve implícitamente None.###
