# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=5665

### Operadores Aritméticos ###

# Operaciones con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print("10 % 3 =", 10 % 3) #operador de módulos, te da el RESTO de la división, y por tanto puede servir para saber si ¡¡hay un múltiplo!!
print("10 // 3 =", 10 // 3) #nos da el COCIENTE 
print("2 ** 3 =", 2 ** 3)
print("2 ** 3 + 3 - 7 / 1 // 4 =", 2 ** 3 + 3 - 7 / 1 // 4)


### COMPARADORES ###
print(3 != 4)           # verdadero
print(3 == 4)           # falso
print( "aaa" >= "aba")  # falso     ORDENACIÓN ALFABETICA.
print( "aaa" <= "baa")  # verdadero
print( "Hola" <= "Py")  # verdadero
print ( "aaa" == "AAA") # falso
print ( "aaa" < "AAA")  # falso
print ( "aaa" > "AAA")  # Verdadero
print (len("Python") < len("aaaaaaaaaaaa")) # Verdadero. Python es más corto que aaaaaaaaaaaa

  
#    Declare your age as integer variable
print("My age is", 25)
print (type(25))
#    Declare your height as a float variable
print ("my high is ", 1.85, " cm")
print (type(1.85))
#    Declare a variable that store a complex number
complex = 1 + 1j; print(complex)
print (type(complex))
#    Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

#    Enter base: 20
#    Enter height: 10
#    The area of the triangle is 100

#Imprime un rango del 0 al 10 pero solo los números divisibles por 3.
rango10=range(0,11)
for numero in rango10:
    if numero%3==0:
        print(numero)

#Imprime un rango pero empezando por el 3 y sea de 2 en 2.
rango3_10=range(3,11,2)
for numero in rango3_10:
    print(numero)


