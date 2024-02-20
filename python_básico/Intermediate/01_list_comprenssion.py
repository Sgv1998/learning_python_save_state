# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=3239

### List Comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

# Definición

my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)


def sum_five(number):
    return number + 5


my_list = [sum_five(i) for i in range(8)]
print(my_list)

"List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list."
"List comprehension is considerably faster than processing a list using the for loop."
"the sintaxis is    -->          [i for i in iterable if expression]"

print("example1")
### 1. For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them:
# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

print("example2")
### 2. For instance if you want to generate a list of numbers
# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]



""" RETO quiero que juntemos cada nombre con su apellido pero manteniendolo dentro de una misma lista (recuerda que [] es una lista)"""
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]



# List comprehension para concatenar los nombres
concatenated_names = [' '.join(name[0]) for name in names]

# Imprime la lista de nombres concatenados
print(concatenated_names)