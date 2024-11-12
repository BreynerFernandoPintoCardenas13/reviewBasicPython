subjects=int(input("enter the number of subjetc what you study: "))
total=0
for i in range(subjects):
    i+=1
    nota=float(input(f"enter the grade of the suject {i}: "))
    if nota>=60:
        print("Lets go bro tou aprove the subjetc")
        total+=3
    else:
        print("hell bro what your doing whit your life?")
        total+=0
if total/i or total>3:
    print(f"Congratulations the numbers of credits then you have is {total}")
else:
    print(f"whats up men, the credits of you have is {total}") 