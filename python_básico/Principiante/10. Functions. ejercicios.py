##Declare a function add_two_numbers. It takes two parameters and it returns a sum
def dos_valores(value1, value2):
    sum=value1+value2
    return sum
print("The sum is: ", dos_valores(5,67))

### Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def radius_circle(r):
    area_circle=round(3.14 * r * r,2)
    return area_circle
print("El area de círculo es ", radius_circle(45))

### Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def season(month):
    if month == 12 or month == 1 or month == 2:
        return "We are at Winter"
    elif month in range(3, 6):
        return "We are at Spring"
    elif month in range(6, 9):
        return "We are at Summer"
    elif month in range(9, 12):
        return "We are at Autumn"
    else:
        return "Invalid month"
print(season(4))

def check_season(month):
    month_lower=month.lower() # Convertir el mes a minúsculas para una comparación sin distinción de mayúsculas
    winter_months = ['december', 'january', 'february']     # Definir los meses asociados con cada estación
    spring_months = ['march', 'april', 'may']
    summer_months = ['june', 'july', 'august']
    autumn_months = ['september', 'october', 'november']
    if month_lower in winter_months:
        return "Winter isn't coming, because it's here"
    elif month_lower in spring_months:
        return "Spring"
    elif month_lower in summer_months:
        return "Summer"
    elif month_lower in autumn_months:
        return "Autumn"
    else:
        return "Invalid value"
print(check_season("APRIL"))

"""
month=input("what month do you like the most") # Verificar si la entrada es una palabra
if month.isalpha():
    check_season_resu=check_season(month)
    print(check_season_resu)
elif month.isdigit():           # Verificar si la entrada es un número 
    season_resu=season(int(month))  #El input() recoge información en forma str (aunque parece que .isdigit no le afecta) por lo que hace falta el int.
    print(season_resu)
else: print("invalid value, try to use one word or just a number like 9")
"""

### Call your function is_empty, it takes a parameter and it checks if it is empty or not ###

def is_empty(data):
    """
    Check if the given data is empty.
    """
    if data is not "":
        return False
    else:
        return True
print(is_empty("[]"))

### This code seems to be checking if the input data is not an empty string. While this will work for strings, it might not cover all
#  cases of empty data, depending on the expected data types. For example, it won't work for empty lists, dictionaries, 
# or other data structures.
print("a better alternative")
def is_empty(data):
    """
    Check if the given data is empty.
    """
    return not data

# Example usage:
print(is_empty("ah"))  # False
print(is_empty(""))    # True
print(is_empty([]))    # True
print(is_empty({}))    # True
print(is_empty(1))    # False
