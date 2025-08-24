#Con un ciclo for, cuenta cuántas vocales (sin distinción de mayúsculas/minúsculas) hay en la frase frase = \"programacion es divertida\" y muestra el total.

frase = "programacion es divertida"
contador = 0
for c in frase.lower():
    if c in "aeiou":
        contador += 1
print(contador)