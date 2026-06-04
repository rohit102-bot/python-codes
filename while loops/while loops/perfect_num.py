num=int(input("enter any number:"))
s=0
i=1

while i<num:
    if num%i==0:
        s=s+i
    i+=1
        
if s==num:
    print("number is a perfect number")

else:
    print("not a perfect number")