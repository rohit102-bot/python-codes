def smartDiv(f):
    def newDiv(n1,n2):
        if n2==0:
            return 0
        else:
            return f(n1,n2)
    return newDiv

@smartDiv
def div(n1,n2):
    n3=n1/n2
    return n3

a=int(input("enter first number"))
b=int(input("enter second number"))
c=div(a,b)
print(f"{a}/{b}={c:2f}")