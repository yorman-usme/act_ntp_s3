#Utilizando un ciclo while, solicita al usuario que ingrese edades una a una. El proceso termina cuando se introduzca -1. Al final, muestra la edad mayor que se haya ingresado.

mayor = -1
edad = int(input("Ingrese una edad (-1 para terminar): "))
while edad != -1:
    if edad > mayor:
        mayor = edad
    edad = int(input("Ingrese una edad (-1 para terminar): "))
print(mayor)