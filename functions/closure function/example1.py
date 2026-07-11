def calculator():
    n1=int(input("enter the forst number: "))
    n2=int(input("enter the seond number: "))
    opr=input("enter the opration")
    def add():
        res=n1+n2
        return res
    def sub():
        res=n1-n2
        return res
    def mul():
        res=n1*n2
        return res
    def div():
        res=n1/n2
        return res
    
    if opr=='+':
        print(f"addition is :{add()}")
    elif opr=='-':
        print(f"substraction is :{sub()}")
    elif opr=='*':
        print(f"multiplication is:{mul()}")
    elif opr=='/':
        print(f"division is : {div()}")
    else:
        print("please give appropriate input ")
    
calculator()
