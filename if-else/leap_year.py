year=int(input("enter the year:"))
if year % 4==0 or year % 400==0:
    print("this is a leap year")
elif year % 100==0:
    print(f"{year} not a leap year")
else:
    print(f"{year} is not a leap year")