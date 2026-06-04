user=str(input("enter the user name:"))
if user=="nit":
    passwd=int(input("enter the passwd"))
    if passwd==123:
        print("wecome")
    else:
        print("incorrect password")
else:
    print("unauthorized user")