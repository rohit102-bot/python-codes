list1=[4,9,2,3,5,1,11,13,17,23,8,12,16,18,20,22,45,15,2,4,66,45,45,58,54]
#without list comprehension 
e=[]
o=[]

for i in list1:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(e)
print(o)

even=[n for n in list1 if n%2==0]
odd=[n for n in list1 if n%2!=0]

print(even)
print(odd)