### retos ###

"""
Ejercicio.1. EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

number=range(1, 101)
def fizz_buzz_script (number):
    for i in number:
        if i%3==0 and i%5==0:
            print("FIZZBUZZ")
        elif i%3==0:
            print("FIZZ")
        elif i%5==0:
            print("BUZZ")
        else:
            print(i)

fizz_buzz_script(number)

""" EJercicio.2. ¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_it_an_anagram(word1, word2):
    if  word1.lower()==word2.lower():
        return False
    elif sorted(word1.lower()) == sorted(word2.lower()):
        return f"Indeed, \"{word1}\" and \"{word2}\" are anagrams"

print(is_it_an_anagram("ana","Aan"))
"""
word1=input("Tell me a word: ")
word2=input("Tell me another word to confirm if it is an anagram of the first one: ")

word1_upper=word1.upper
word2_upper=word2.upper

word1list=set(word1_upper)
word2list=set(word2_upper)
if word1list==word2list:
    print("\t {word1} IS an anagram if {word2}")
    print(word1list, word1)
    print(word2list, word2)
else:
    print(f"\t {word1} is NOT an anagram of {word2}")
    print(word1list, word1)
    print(word2list, word2)
"""

"""
Ejercicio.3. Sucesión de Fibonacci.
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""




def fibonacci(start):
   prev=0
   next=1
   for i in range(start,start+20):
       prev=i
       fibosuma= prev + next
       prev = next
       next = fibosuma
       print(prev, "fibonacci")
print (fibonacci(0,7))










""" prueba fallida
def fibonacci(number):
   number=0
   for i in range(0,51):
       number2=number
       number=i
       print(number2+number)
print (fibonacci(0))
"""

""" No funciono
lista_fibo=list()
def fibonacci(number=1):
    while number<1000:
        lista_fibo.insert(number)
        number=number+lista_fibo[-1]
        return number
    else:
        return "se alcanzo el límite de esta máquina"

print(fibonacci(1))
"""
