#Utilizando un ciclo while, simula un reloj digital que muestre cada segundo desde 00:00 hasta 00:59 en formato MM:SS, cada valor en una línea.

m, s = 0, 0
while s < 60:
    print(f"{m:02}:{s:02}")
    s += 1