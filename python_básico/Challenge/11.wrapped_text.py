"""You are given a string and width .
Your task is to wrap the string into a paragraph of width

Function Description
Complete the wrap function in the editor below.
wrap has the following parameters:
    string string: a long string
    int max_width: the width to wrap to

Returns
    string: a single string with newline characters ('\n') where the breaks should be

Input Format
The first line contains a string,
The second line contains the width, .

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""


def wrap(string, max_width):
    wrapped_text = ''
    for i in range(0, len(string), max_width):          # ahora i tomará valores de 4 en 4 (max_width)
        wrapped_text += string[i:i+max_width] + '\n'    #Toma las posiciones i a i+width del string, y les añade un punto aparte,
                                                        # esto lo añade al nuevo texto "wrapped_text" que es el que se imprime.
    return wrapped_text

string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4
result = wrap(string, max_width)
print(result)

""" La función wrap toma dos argumentos: string (la cadena que queremos envolver) y max_width (la longitud máxima de cada línea).
    Dentro de la función, wrapped_text es una cadena vacía donde almacenaremos la cadena envuelta.
    El bucle for itera sobre la cadena string con un paso de longitud max_width. En cada iteración, 
        se agrega una porción de la cadena de max_width caracteres a wrapped_text, seguido de un carácter 
        de nueva línea ('\n'), lo que crea una nueva línea en el texto envuelto.
    Una vez que se ha completado el bucle, la función devuelve el texto envuelto.
    Finalmente, la cadena envuelta se imprime usando print(result).

ACLARACIÓN
La línea wrapped_text += string[i:i+max_width] se encarga de agregar una porción de la cadena original string a la cadena envuelta wrapped_text.

Voy a descomponer esa línea en partes más pequeñas para que sea más claro:

    string[i:i+max_width]: Esta parte toma una porción de la cadena original string, empezando en el índice i y terminando 
    en el índice i+max_width. Es decir, selecciona max_width caracteres de la cadena string, comenzando desde la posición i.

    Por ejemplo, si string es "ABCDEFGHIJKLIMNOQRSTUVWXYZ" y max_width es 4, en la primera iteración, i sería 0, por lo 
    que string[i:i+max_width] sería "ABCD". En la segunda iteración, i sería 4, por lo que string[i:i+max_width] sería 
    "EFGH", y así sucesivamente.

    wrapped_text += ...: Esta parte agrega la porción seleccionada de la cadena original string a la cadena envuelta 
    wrapped_text. El operador += se utiliza para agregar el resultado de string[i:i+max_width] al final de la cadena wrapped_text.

Entonces, en resumen, esta línea está construyendo la cadena envuelta agregando segmentos de longitud max_width de la 
cadena original string en cada iteración del bucle. Cada segmento corresponde a una línea en el texto envuelto.
"""

### TEXT WRAP ###
"""
The textwrap module provides two convenient functions: wrap() and fill().

#textwrap.wrap()
The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most.
It returns a list of output lines.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 

#textwrap.fill()
The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.
"""