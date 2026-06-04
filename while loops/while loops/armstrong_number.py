num=input("enter any number:")
org=int(num)
l=len(num)
s=0
num=int(num)
while num>0:
    d=num%10
    s=s+(d**l)
    num=num//10

if org==s:
    print("number is armstrong number")

else:
    print("number is not armstrong ")
    

