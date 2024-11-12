distance=float(input("enter the distance: "))
kmH=float(input("enter the velocity of your have: "))
if kmH>120:
    print("CAREFUL YOU SPEED IS TO MUCH")
else: 
    time=distance/kmH
    hours=int(time)
    minuts=round(time-hours)*60
    print(f"you travel is {hours}hours and {minuts}minutes")