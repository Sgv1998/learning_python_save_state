# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=21442

### Conditionals ###

# if

my_condition = False

if my_condition:  # Es lo mismo que if my_condition == True:   lo que significa, que contiene algo o lo que contiene es cierto
    print("Se ejecuta la condición del if")
else:
    print ("Es falso my_condition") 

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

# if, elif, else

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

# Condicional con ispección de valor

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")


### EJERCICIOS ###
print("\n EJERCICIOS")
""""
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.

"""
"""
        # Mi solución #
age_str= input("Enter your age: ")
age=int(age_str)
if age>18:
    print ("You are old enough to learn to drive")
else:   print("You need {} more years to learn to drive".format(18-age))
"""
"""
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) 
to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, 
and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
"""



"""
# Mi solución para discutir quien es mayor y por cuanto #
my_age=25
your_age_str2= input("Enter your age: ")
your_age=int(your_age_str2)
if your_age >= my_age:
    if your_age>my_age: 
        print(f"You are {your_age-my_age} years older than me")) 
    elif your_age-my_age==1: 
        print("You are 1 year older than me")
    else: print("We share the same age")

if your_age<my_age:print("I am {} years older than you".format(-(your_age-my_age)))
elif my_age-your_age==1: print("I am 1 year older")


month_your_age_rest= your_age%1  #Queria intentar una condicion de si el resto es|=0 que tambien indicque la dif de años y meses.
"""
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
            'street': 'Space street',
            'zipcode': '02210'
    }
    }
""" Check if the person dictionary has skills key, if so print out the middle skill in the skills list."""

if person.keys()==" ":
    print("The dicctionary has no keys")
else:
    print("The dictionary has keys: ", person.keys())
    print("From the key: skills, its middle value is: ", person['skills'][2])


"""* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result."""
if person['skills']==" ":
    print(f"The dicctionary has no values for the KEY: {person['skills']}")
    
else:
    print("The dictionary has values in the key word: \"skills\"")
    if "Python" in person['skills']:
        print("And the key: \"skills\" in the dictionary \"person\" conteins the word \"Phyton\"")

"""* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, 
 MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
 else print('unknown title') - for more accurate results more conditions can be nested!"""

if "JavaScript" and "React" in person["skills"]:
    print ('He is a front end developer')
if "Node" and "Python" and "MongoDB" in person["skills"]:
    print('He is a backend developer')
if "React" and "Node"  and "MongoDB" in person["skills"]:
    print('He is a fullstack developer')
else:
    print('unknown title')


""" * If the person is married and if he lives in Finland, print the information in the following format:"""


#basura
"""
número_keys=len(person.keys)*0.5
print(número_keys)
if person.keys()==True:print(person.key[número_keys])
"""