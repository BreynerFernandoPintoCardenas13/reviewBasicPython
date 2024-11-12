n = int(input("Ingresa un número entero positivo: "))

if n <= 0:
    print("Por favor, ingresa un número positivo mayor que 0.")
else:
    suma = 0
for i in range(1, n + 1):
    suma += i
print(f"La suma de los primeros {n} números enteros es: {suma}")
