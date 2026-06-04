num=int(input("enter the the number:"))
sum=0
if num==0:
    sum=0
else:
    while num>0:
        digit=num%10 #get the didgit
        num=num//10 #cut the ddigit to make condition false
        sum=digit+sum #add digit in sum

print(sum)