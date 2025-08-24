#Con un ciclo for, cuenta cuántas letras 'a' (minúscula) hay en la cadena texto = \"manzana\" y muestra el total.

texto = "manzana"
contador = 0
for c in texto:
    if c == "a":
        contador += 1
print(contador)