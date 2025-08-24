#"Utilizando un ciclo while, solicita al usuario que ingrese números. El proceso termina cuando el usuario escriba 0. Al final, muestra la suma total de todos los números ingresados.

suma = 0
num = int(input("Ingrese un número (0 para terminar): "))
while num != 0:
    suma += num
    num = int(input("Ingrese un número (0 para terminar): "))
print(suma)