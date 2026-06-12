#without comprehesion
list1=[1,2,3,-5,4,-89,55,42,-22,25,-54,18,-56,89,-21]
pos=[]
neg=[]

for i in list1:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)
print(f"positive numbers in list are: {pos}")
print(f"negative numbers in list are: {neg}")

#with comprehension

pos2=[i for i in list1 if i>0]
neg2=[i for i in list1 if i<0]

print(pos2)
print(neg2)