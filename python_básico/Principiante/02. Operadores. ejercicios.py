#    Declare your age as integer variable
print("My age is", 25)
print (type(25))
#    Declare your height as a float variable
print ("my high is ", 1.85, " cm")
print (type(1.85))
#    Declare a variable that store a complex number
complex = 1 + 1j
print(complex)
print (type(complex))

""" <- borra las comillas para ver esta parte. es que se pone a preguntar por cada INPUT jajaja.
#    Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
h=float(input("height of the triangle "))   # Enter height: 10
b=float(input("base of the triangle "))   # Enter base: 20
high=h
base=b
area_tri=(high*base/2)
print(area_tri, " is the area of your triangle.")  #    The area of the triangle is 100


###Get length and width of a rectangle using prompt. Calculate its area (area = length x width) 
# and perimeter (perimeter = 2 x (length + width))###
lenght_rect=float(input("lenght of the rectangle "))   
width_rect=float(input("width of the rectangle "))  
area_r=lenght_rect*width_rect
perimeter_r=2*lenght_rect+width_rect
print("area is = ", area_r, " and the perimeter is = ", perimeter_r)


### "I hope this course is not full of jargon". Use "in" operator to check if "jargon" is in the sentence.
finder=str(input("Which word are you looking for "))     #jargon
print("we can say that is ", finder  in "I hope this course is not full of jargon")
"""
###There is no 'on' in both dragon and python
print("on"  in ("jargon" and "drag on"))
print("Both words contain 'on'!" if 'on' in ('dragon' and 'python') else "No 'on' in both words.")

### Find the length of the text python and convert the value to float and convert it to string

Longitud_python=(len("python"))
print(Longitud_python)
print(type(Longitud_python))
print(type(float(Longitud_python)))
print(type(str(float(Longitud_python))))

###Check if type of '10' is equal to type of 10
print("type('10' is 10) is", type('10') is type(10))

###Check if int('10') is equal to 10
number10:int='10'
print("int('10') is equal to 10", number10 is 10)

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8,)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)
print("Se me ha ocurrido esta segunda opción con comillas")
print("""1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125""")