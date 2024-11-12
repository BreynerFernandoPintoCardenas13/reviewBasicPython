hour = float(input("Enter the number of hours in the parking: "))

total_cost = 0

if hour <= 1:

    total_cost = 5

    print(f"You spent ${total_cost} in the parking.")

elif 2 <= hour <= 4:

    total_cost = 5 + (hour - 1) * 4

    print(f"You spent ${total_cost} in the parking.")

else:

    total_cost = 5 + 3 * (hour - 4) + 12

    print(f"You spent ${total_cost} in the parking.")