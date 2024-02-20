"""Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example: records=[["c", 20],["b", 50],["a",50]
The ordered list of scores is [20, 50], so the second lowest score is 50. There are two students with that score: ["b", "a"]. Ordered alphabetically, the names are printed as: 
a
b

Y además el programa usa un input para introducir datos aleatorios para ver que el codigo funciona en otros casos. Siendo el código (name, para los nombres; score, para la puntuación):
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())"""


score=[5, 37.21, 37.21, 37.2, 41, 39]
name=["Harry", "Berry", "Tina", "Akriti", "Harsh"]

records=dict()
records.append(score,name)       #INTENTO FALLIDO
print(records)
records_sorted=records.sort()
print(records_sorted)

for record in records_sorted:
    print(record[0])
    print(record[1])

"""
dict[name] = score
print(name)

scores = list(dict.values())
scores.sort()
second_lowest_score = [x for x in scores if x>scores[0]][0]
name = [i for i in dict if dict[i] == second_lowest_score]
name.sort()
for i in name:
    print(i)

"""




"""
records=[]
records.append([score, name])
print(records)
records_sorted=records.sort()
print(records_sorted)

for record in records_sorted:
    print(record[0])
    print(record[1])
"""