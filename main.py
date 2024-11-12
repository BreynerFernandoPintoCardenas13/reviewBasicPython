year=int(input("enter a year:"))
if year%4==0 or year%400==0: 
    print("your year is leap")
else:
    print("your year is not leap")