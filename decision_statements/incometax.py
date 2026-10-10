name = input("enter your name:")
salary= int(input("enter your salary:"))

if salary >400000 and salary <= 800000:
    print("----")
    print(f"name:{name}")
    Income_Tax = salary * 0.05
    print(f"total tax to pay  is :{Income_Tax}")

elif salary>800000 and salary<= 1200000 :
    print("----")
    print(f"name:{name}")
    Income_Tax = salary * 0.10
    print(f"total tax to pay is is :{Income_Tax}")
elif salary>1200000 and salary<= 1600000 :
    print("----")
    print(f"name:{name}")
    Income_Tax = salary * 0.15
    print(f"total tax to pay is is :{Income_Tax}")
elif salary > 1600000 and salary <= 2400000 :
    print("----")
    print(f"name:{name}")
    Income_Tax = salary * 0.20
    print(f"total tax to pay is is :{Income_Tax}")

else :
    Income_Tax = salary * 0.25
    print(f"total tax to pay is :{Income_Tax}")