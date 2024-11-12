height=float(input("enter you height in meters: "))
weight=float(input("enter you weight in kg: "))
imc= weight/height**2
if imc<18.5:
    print("you underweight")
elif imc>18.5 and imc<=24.9:
    print("you weight its normal")
elif imc>18.5 and imc<24.9:
    print("you weight its normal")
elif imc>24.9 and imc<29.9:
    print("you weight its high weight")
elif imc>=30:
    print("you weight its overweight")
else:
    print("try again")
