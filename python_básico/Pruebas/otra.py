text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index=alphabet.find(text[3])
print(index)

"""index = alphabet.find(text[3]): Aquí se utiliza el método find en la cadena alphabet para encontrar la posición del cuarto carácter (índice 3) de la cadena text en el alfabeto.

    text[3] es 'l', ya que la indexación en Python comienza desde 0.
    alphabet.find('l') buscará la posición de 'l' en la cadena alphabet.

Entonces, el valor de index será la posición de 'l' en el alfabeto, que es 11"""