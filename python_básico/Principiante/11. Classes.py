# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###

# Definición: 
"""clase es una plantilla para la creación de objetos. Los objetos son instancias de clases, 
y las clases definen atributos y comportamientos comunes a todos los objetos creados a partir de ellas. 
En otras palabras, una clase es un plano o un modelo a partir del cual se crean objetos.
Ejemplo de Moure, clase ave, a ella asociamos, ala, plumas, volar, pero no dientes o reptar"""

class MyEmptyPerson:                 #Norma Escritura para class: Escribimos junto y Mayuscula la primera letra de cada palabra
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas
class Person0:
    def __init__(self, name0, surname0):
        self.name = name0;           #Propiedad pública
        self.surname = surname0      #Propiedad pública
        self.fullname= f"{name0} {surname0}"        #Propiedad pública
        
my_person0 = Person0("Paco", "Rodriguez")
print(f"{my_person0.name} {my_person0.surname}")
print(my_person0.fullname)
        

class Person:       
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure")    # sin el (brais  moure) daría error, y añade esta información a name y surname.
print(my_person.full_name)
print(my_person.get_name())     #yo: esto es para extra
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)