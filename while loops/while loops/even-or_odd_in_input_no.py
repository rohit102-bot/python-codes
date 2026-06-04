num=int(input("enter the number : "))
evenc=0
oddc=0

while num>0:
    d=num%10
    num=num//10
    if d%2==0:
        evenc+=1
    else:
        oddc+=1

print (f"even:{evenc}  oddcount:{oddc}")
