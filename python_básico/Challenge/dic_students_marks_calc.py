"""Me han pedido hacer lo siguiente en python:

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal. 

The first line contains the integer n, the number of students' records. The next n lines contain the names and marks obtained 
by a student, each value separated by a space. The final line contains query_name, the name of a student to query.
"""


# La solución para el reto de hackerrank

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

"""
The inputs --> 
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika


Expected output --> 56.00 for Malika
"""


query_scores = student_marks.get(query_name, [])
average_mark = sum(query_scores) / len(query_scores) if query_scores else 0      #If query_scores es por si contiene datos= TRUE. En caso contrario (else) poner 0.
print("{:.2f}".format(average_mark))


"""
Certainly! Let's go through the code step by step:

1. `n = int(input())`: Reads an integer `n` representing the number of students' records.

2. `student_marks = {}`: Initializes an empty dictionary `student_marks` to store the name and marks of each student.

3. `for _ in range(n):`: Iterates through the range of `n` to read the names and marks of each student.

   a. `name, *line = input().split()`: Reads a line of input where the first element is the student's name, and the remaining elements 
   are the marks. The `*line` is used to collect all the remaining elements into a list.

   b. `scores = list(map(float, line))`: Converts the list of marks from strings to floats using `map` and `float`. This list of floats 
   is assigned to the variable `scores`.

   c. `student_marks[name] = scores`: Stores the student's name as the key and their list of marks as the value in the `student_marks` 
   dictionary.

4. `query_name = input()`: Reads the name of the student for whom the average marks need to be calculated.

5. Calculate and print the average marks for the specified student:

   a. `query_scores = student_marks.get(query_name, [])`: Retrieves the list of scores for the specified student using `get`. 
   If the student is not found, it returns an empty list.

   b. `average_mark = sum(query_scores) / len(query_scores) if query_scores else 0`: Calculates the average of the marks using 
   the `sum` and `len` functions. If `query_scores` is not empty, it calculates the average; otherwise, it sets the average to 0 to 
   avoid division by zero.

   c. `print("{:.2f}".format(average_mark))`: Prints the average marks with two decimal places using string formatting.

So, the code reads input data about students, stores it in a dictionary, and then calculates and prints the average marks for the 
specified student.
"""



# Haciendo pruebas por mi cuenta

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = {"Krishna":{67, 68, 69},"Arjun": {70, 98, 63},"Malika": {52, 56, 60}}.split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

"""
The inputs --> 
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Intente meterlo como así:
(["Krishna", 67, 68, 69],["Arjun", 70, 98, 63],["Malika", 52, 56, 60])   listaS
{"Krishna":{67, 68, 69},"Arjun": {70, 98, 63},"Malika": {52, 56, 60}}   diccionario
"""


query_scores = student_marks.get(query_name, [])
average_mark = sum(query_scores) / len(query_scores) if query_scores else 0      #If query_scores es por si contiene datos= TRUE. En caso contrario (else) poner 0.
print("{:.2f}".format(average_mark))