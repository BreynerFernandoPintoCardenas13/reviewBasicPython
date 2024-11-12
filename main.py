inicio = int(input("Ingresa el valor de inicio: "))
fin = int(input("Ingresa el valor de fin: "))

for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        print(numero)