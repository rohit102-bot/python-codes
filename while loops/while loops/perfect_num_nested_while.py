a=int(input("enter the starting value: "))
b=int(input("enter the ending value: "))

while a<=b:
    i=1
    s=0
    while i<a:
        if a%i==0:
            s=s+i
        i=i+1
    if s==a:
        print(a)
    a=a+1