#Con un ciclo for, solicita al usuario que ingrese un número entero positivo y calcula la suma de sus dígitos, mostrando el resultado final.

n = input("Ingrese un número entero positivo: ")
suma = 0
for d in n:
    suma += int(d)
print(suma)