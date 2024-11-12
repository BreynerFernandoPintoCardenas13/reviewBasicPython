suma = 0

while True:
    numero = int(input("Ingresa un número entero: "))    
    if numero % 2 != 0:
        break
    suma += numero
    print(f"La suma de los números pares es: {suma}")