cadena = input("Ingresa una cadena de texto: ")
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra.lower() in vocales:
        contador += 1

print(f"La cantidad de vocales en la cadena es: {contador}")