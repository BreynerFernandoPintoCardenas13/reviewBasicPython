desicion=int(input(f"if you want convert the temperature to celsius enter [1]\nif you want convert to farenheit[2]\n"))
def grades(lista):
    match lista:
        case [1]:
            gradesIn=float(input("enter a temperature in farhenheit:"))
            conversion=(gradesIn-32)*(5/9)
            return f"the conversion is: {conversion}"
        case [2]:
            gradesIn=float(input("enter a temperature in celsius:"))
            conversion=gradesIn*(9/5)+32
            return f"the conversion is:{conversion}"

print(grades([desicion]))  # Salida: "Lista con tres elementos: 1, 2, 3"
