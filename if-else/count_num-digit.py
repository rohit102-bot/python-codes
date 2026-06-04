num=int(input("enter any number: "))
c=0 #count
if num==0:
    c=1
else:
    while num>0:
        num=num//10 #num=123 1st itr=12,c=1 2nd itr=1,c=2 3rd itr=0,c=3
        c=c+1

print(c)