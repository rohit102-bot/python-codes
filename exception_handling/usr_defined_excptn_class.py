class UsrError(Exception):
    def __str__(self):
        return "this is user defined excptn"

def multiply(n1,n2):
    if n1==0 or n2==0:
        #raise ValueError #predefined exception class
        raise UsrError #user defined exception class
    else:
        return n1*n2

try:
    num1=int(input("enter num1: "))
    num2=int(input("enter num2: "))
    num3=multiply(num1,num2)
    print(num3)
except ValueError: 
    print("number should not be zero")
except UsrError as a:
    print(a)