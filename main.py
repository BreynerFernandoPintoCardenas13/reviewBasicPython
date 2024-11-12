import random
print("im think in a random number, guess")
numberTwo=0
number=random.randint(1, 10)
while numberTwo!=number:

    numberTwo=int(input("enter the number: "))
    if numberTwo<number:
        print("the number is more higher")
    elif numberTwo>number:
        print("the number is more lower")

print(f"you guess the number was {number}")