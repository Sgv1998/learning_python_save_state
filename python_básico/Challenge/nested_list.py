# Lista de claves
keys = ["nombre", "edad", "ciudad"]

# Lista de valores
values = ["Juan", 25, "Madrid"]

# Inicializar el diccionario vacío
mi_diccionario = {}

# Iterar sobre las listas de claves y valores
for i in range(len(keys)):
    # Asignar la clave y el valor al diccionario
    mi_diccionario[keys[i]] = values[i]

# Imprimir el diccionario resultante
print(mi_diccionario)

####################################################################################
# Listas de puntuaciones y nombres
scores = [37.21, 37.21, 37.2, 41, 39]
names = ["Harry", "Berry", "Tina", "Akriti", "Harsh"]

# Inicializar el diccionario vacío
student_dict = {}

# Crear el diccionario con las puntuaciones y nombres

for i in range(len(scores)):
    student_dict[names[i]] = scores[i]

# Ordenar el diccionario por puntuaciones y obtener la segunda puntuación más baja
sorted_students = sorted(student_dict.items(), key=lambda x: x[1])
second_lowest_score = sorted(set(score for _, score in sorted_students))[1]

# Filtrar los nombres de los estudiantes con la segunda puntuación más baja
second_lowest_students = sorted([name for name, score in sorted_students if score == second_lowest_score])

# Imprimir los nombres en orden alfabético
for student in second_lowest_students:
    print(student)

# NOTAS para aclarar dudas: 
### Entonces, range(len(scores)) se utiliza para generar una secuencia de números que puedes utilizar como índices para 
    ### iterar sobre los elementos de la lista scores. En el contexto del código que proporcioné anteriormente, i toma los valores
    ###  de 0 hasta la longitud de scores menos 1, y se utiliza para acceder a los elementos correspondientes en las listas scores y
    ### names. Esto permite construir el diccionario asociando las puntuaciones con los nombres de los estudiantes.

### 1. "sorted(student_dict.items(), key=lambda x: x[1])"": Aquí, "student_dict.items()" retorna una vista de tuplas que contiene 
    ### (clave, valor) para cada elemento en el diccionario "student_dict". La función "sorted" ordena estas tuplas según el segundo 
    ### elemento ("x[1]"), que es la puntuación del estudiante. Esto significa que "sorted_students" será una lista de tuplas ordenadas por 
    ### puntuación de menor a mayor.
    
### 2. "set(score for _, score in sorted_students)"": Aquí, estamos utilizando una expresión de generador para extraer las puntuaciones de
    ### "sorted_students", pero estamos ignorando las claves (nombres de los estudiantes) usando "_" como un marcador de posición. Luego, 
    ### convertimos estas puntuaciones en un conjunto ("set"), eliminando así las duplicadas.

### 3. "sorted(...)[1]": Finalmente, ordenamos el conjunto de puntuaciones (que ahora es único y está ordenado de menor a mayor) y 
    ### tomamos el segundo elemento ([1]), que es la segunda puntuación más baja.

### OTRA FORMA ###
print("otra forma")

scores = [37.21, 37.21, 37.2, 41, 39]
names = ["Harry", "Berry", "Tina", "Akriti", "Harsh"]

# Inicializar el diccionario vacío
student_dict = {}

# Crear el diccionario con las puntuaciones y nombres:           
### Al utilizar zip(names, scores), estamos creando pares de elementos de las dos listas, lo que simplifica 
### el proceso de construcción del diccionario. Lamento la confusión y espero que esto resuelva el problema.
for name, score in zip(names, scores):
    student_dict[name] = score

# Ordenar el diccionario por puntuaciones y obtener la segunda puntuación más baja
sorted_students = sorted(student_dict.items(), key=lambda x: x[1])
second_lowest_score = sorted(set(score for elbicho, score in sorted_students))[1]

# Filtrar los nombres de los estudiantes con la segunda puntuación más baja
second_lowest_students = sorted([name for name, score in sorted_students if score == second_lowest_score])

# Imprimir los nombres en orden alfabético
for student in second_lowest_students:
    print(student)
