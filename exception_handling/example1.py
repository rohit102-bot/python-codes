n1=int(input("enter the first number:"))
n2=int(input("enter the second number: "))
try:
    n3=n1/n2
    print(n1,n2,n3)

except ZeroDivisionError:
    print("cannot divide number with zero")