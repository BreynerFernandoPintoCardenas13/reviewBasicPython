exit=1
while exit:
    number=float(input("enter a number: ")) 
    numberTwo=float(input("enter a number: "))
    operator=input("enter a operator: ")
    if operator=="+":
        plus=int(number+numberTwo)
        print(f"the rest is {plus}")
    elif operator=="-":
        plus=int(number-numberTwo)
        print(f"the rest is {plus}")
    elif operator=="*":
        plus=number*numberTwo
        print(f"the rest is {plus}")
    elif operator=="/":
        plus=number/numberTwo
        print(f"the rest is {plus}")
    else:
        print("no valido")

    exit=int(input(f"if yo want continue enter [1]\nif you dont want enter[0]\n"))
    