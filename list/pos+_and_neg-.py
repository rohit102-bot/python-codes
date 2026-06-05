list1=[1,23,5,6,-1,6,-8,-7,10]
pos=[]
neg=[]

for i in range(len(list1)):
    if list1[i]<0:
        neg.append(list1[i])
    else:
        pos.append(list1[i])
print(f"positive numbers are {pos}")
print(f"negative numbers are {neg}")
