while True:
    grade=float(input("enter the grade: "))
    bonification=input("you did adicional task? Answer yes or no: ")
    if bonification.lower()=="yes":
        operation=((5/100)*grade)+grade
        if operation>100:
            print(f"Great, with the adicional task your final grade is: 100")
            break
        else:
            print(f"Great, with the adicional task your final grade is: {operation}")
            break
    elif bonification.lower()=="no":
        print(f"Okey you final grade is: {grade}")
        break
    else:
        print("try again and follow the instructions")
        