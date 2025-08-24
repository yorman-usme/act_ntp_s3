#Mediante un ciclo while, solicita al usuario que escriba palabras. El proceso termina cuando el usuario escriba la palabra \"fin\". Al final, muestra cuántas palabras se leyeron (sin contar \"fin\").

contador = 0
palabra = input("Escriba una palabra (fin para terminar): ")
while palabra != "fin":
    contador += 1
    palabra = input("Escriba una palabra (fin para terminar): ")
print(contador)