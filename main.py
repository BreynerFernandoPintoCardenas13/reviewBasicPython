import os
while True:    
    sideOne=float(input(f"enter the side 1:"))
    sideTwo=float(input(f"enter the side 2:"))
    sideThree=float(input(f"enter the side 3:"))
    if sideOne<90 and sideTwo<90 and sideThree<90:
        print("the triangle is Agudo")
    if sideOne==90 or sideTwo==90 or sideThree==90:
        print("the triangle is Rectacle")
    if sideOne>90 or sideTwo>90 or sideThree>90 :
        print("the triangle is Obtuso")
    decision=input("you want try again? Yes=1 or Not=0: ")
    if decision==0:
        break