def primegenerator(start,stop):
    for num in range(start,stop+1):
        c=0
        for i in range(1,num+1):
            if num%i==0:
                c+=1
        if c==2:
            yield num

a=primegenerator(5,20)
#value1=next(a)
#print(value1)
#value2=next(a)
#print(value2)
for value in a:
    print(value,end=" ")