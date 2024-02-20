# The question to solve:
thickness = int(input()) # This must be an odd number
c = 'H'

# Top Cone (looking up)
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars (looking up)
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars (looking down)
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone (looking down)
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# ########

# Top Cone (looking up)
for i in range(thickness):                                                  # Se repetira esta lectura 5 veces
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars (looking up)
for i in range(thickness+1):                                                # Se repetira esta lectura 6 veces
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):                                           # Se repetira esta lectura 3 veces
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars (looking down)
for i in range(thickness+1):                                                # Se repetira esta lectura 6 veces
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone (looking down)
for i in range(thickness):                                                  # Se repetira esta lectura 5 veces
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).ljust(thickness*6))
# thickness-i-1 para invertir la flecha.
# que el texto comience a una distancia = thickness, y las Hs se escriban desde la derecha
# entre medias que aparezca un H
# luego con una distancia = thickness que se escriban las Hs desde la izquierda.
# Todo esto, a una distancia= thickness* 6 --> ").rjust(thickness*6)" por ello ese parentesis engohblando a todo lo anterior.
# Eso sí, si, no funciona si le pones "ljust".
