def multiply(n1,n2):
    if n1==0 or n2==0:
        raise ValueError()
    else:
        return n1*n2

num1=int(input("enter the num1: "))
num2=int(input("enter num2: "))

try:
    num3=multiply(num1,num2)
    print(num3)
except ValueError:
    print("no number should be zero")