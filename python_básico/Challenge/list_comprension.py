"""
Let's learn about list comprehensions! You are given three integers and representing the dimensions of a cuboid along with an integer . 
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Here, . 
Please use list comprehensions rather than multiple loops, as a learning exercise. """

"""use as an example x=1 y=1 z=1 n=2
"""
#mi respuesta )
x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))
z = int(input("Ingrese el valor de z: "))
n = int(input("Ingrese el valor de n: "))

numbers = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
print(numbers)

#Nota: sí, el problema tenía dificultad en primero, encontrar el como se formula una lista comprimida y más concatenando. 
#      seguido por tener muy claro que es lo que te pide el texto, no es que no deba ser superior a N si no que ¡¡ no sume igual a N !!