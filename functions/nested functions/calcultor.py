def calculator(num1,num2,opr):
    res=None
    def add():
        nonlocal res
        res=num1+num2
        return res
    def sub():
        nonlocal res
        res=num1-num2
        return res
    def mul():
        nonlocal res
        res=num1*num2
        return res
    def div():
        nonlocal res
        res=num1/num2
    if opr=='+':
        add()
    if opr=='-':
        sub() 
    if opr=='*':
        mul()
    if opr=='/':
        div()
    return res
    
num1=int(input("enter the number1: "))
opr=input("enter the operator: ")
num2=int(input("enter number2: "))
result=calculator(num1,num2,opr)

print(result)