salary=float(input("put your salary: "))
country=input("select your country write: 'Pais A' 'Pais B' 'Pais C' 'Pais D':\n")
if country.lower()=="pais a":
    taxes=salary-(0.20*salary)
    print(f"your salary with taxes is {taxes}")
elif country.lower()=="pais b":
    taxes=salary-(0.15*salary)
    print(f"your salary with taxes is {taxes}")
elif country.lower()=="pais c":
    taxes=salary-(0.10*salary)
    print(f"your salary with taxes is {taxes}")
