n = int(input("Ingresa un número entero positivo: "))

if n < 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(f"El factorial de {n} es: {factorial}")
