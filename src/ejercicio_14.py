#Mediante un ciclo while, implementa un juego de adivinanza: el programa genera un número aleatorio del 1 al 10 y solicita al usuario que lo adivine. El proceso se repite hasta que el usuario acierte. Muestra un mensaje de felicitación al final.

import random
secreto = random.randint(1, 10)
intento = int(input("Adivina el número (1-10): "))
while intento != secreto:
    intento = int(input("Adivina el número (1-10): "))
print("¡Felicidades, acertaste!")