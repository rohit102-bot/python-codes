import sys 
try:
    n1=int(input("enter the num1: "))
    n2=int(input("enter the num2: "))
    n3=n1/n2
    print(n3)
except:
    t=sys.exc_info()
    print(t[1])