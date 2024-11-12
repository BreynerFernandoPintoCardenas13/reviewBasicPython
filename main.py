i=1
sideOne=float(input(f"enter the side{i}"))
sideTwo=float(input(f"enter the side{i}"))
sideThree=float(input(f"enter the side{i}"))
if sideOne == sideTwo == sideThree:
    print("the triangle is equilatero")
if sideOne != sideTwo != sideThree:
    print("the triangle is escaleno")
if sideOne != sideTwo == sideThree or sideOne == sideTwo != sideThree:
    print("the triangle is isoceles")